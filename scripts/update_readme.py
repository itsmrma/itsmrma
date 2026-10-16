#!/usr/bin/env python3
"""
scripts/update_readme.py

Automatically keeps README.md in sync with repository changes:
1. Detects latest releases and tags (e.g., SyncForge v3.0.0).
2. Inspects remote repositories (languages, manifests like Cargo.toml, package.json, pyproject.toml).
3. Updates marked sections in README.md without modifying any custom prose or structure.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Configured repositories and their stack preferences/tools
REPO_CONFIG = {
    "SyncForge": {
        "owner": "itsmrma",
        "repo": "SyncForge",
        "preferred_tools": ["FFmpeg", "MKVToolNix", "ffsubsync"],
        "version_marker": "syncforge-version",
        "stack_marker": "syncforge-stack",
    },
    "spotify-history-analyzer": {
        "owner": "itsmrma",
        "repo": "spotify-history-analyzer",
        "preferred_tools": ["Material Design 3", "Chart.js", "JSZip", "Playwright"],
        "version_marker": None,
        "stack_marker": "spotify-stack",
    },
}

def github_request(url: str, as_json: bool = True):
    headers = {"User-Agent": "itsmrma-readme-updater"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode("utf-8")
            if as_json:
                return json.loads(content)
            return content
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        print(f"HTTP error fetching {url}: {e.code} {e.reason}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def get_latest_release(owner: str, repo: str):
    data = github_request(f"https://api.github.com/repos/{owner}/{repo}/releases/latest")
    if data and "tag_name" in data:
        return {
            "tag": data["tag_name"],
            "name": data.get("name", data["tag_name"]),
            "url": data.get("html_url", f"https://github.com/{owner}/{repo}/releases/latest"),
        }
    return None

def detect_repo_stack(owner: str, repo: str, config: dict):
    """
    Detects the tech stack of a repository:
    1. Primary programming language from GitHub API.
    2. Frameworks and libraries from Cargo.toml, package.json, pyproject.toml.
    3. Preserves preferred system tools or specialized libraries.
    """
    stack = []
    
    # 1. Primary languages
    langs_data = github_request(f"https://api.github.com/repos/{owner}/{repo}/languages")
    primary_lang = None
    if langs_data and isinstance(langs_data, dict):
        # Sort by byte size descending
        sorted_langs = sorted(langs_data.keys(), key=lambda l: langs_data[l], reverse=True)
        # Exclude markup/style as primary language if real code language exists
        code_langs = [l for l in sorted_langs if l not in ("HTML", "CSS", "SCSS", "Linker Script", "Makefile")]
        if code_langs:
            primary_lang = code_langs[0]

    # Check Cargo.toml (Rust / Tauri)
    cargo_raw = github_request(f"https://raw.githubusercontent.com/{owner}/{repo}/main/src-tauri/Cargo.toml", as_json=False)
    if not cargo_raw:
        cargo_raw = github_request(f"https://raw.githubusercontent.com/{owner}/{repo}/main/Cargo.toml", as_json=False)
    
    is_rust = False
    if cargo_raw:
        is_rust = True
        stack.append("Rust")
        if "tauri" in cargo_raw.lower():
            if 'tauri = { version = "2"' in cargo_raw or 'tauri-build = { version = "2"' in cargo_raw:
                stack.append("Tauri v2")
            else:
                stack.append("Tauri")

    # If primary language wasn't added yet, add it
    if primary_lang and primary_lang not in stack:
        stack.insert(0, primary_lang)

    # Check package.json (Frontend / Node)
    pkg_raw = github_request(f"https://raw.githubusercontent.com/{owner}/{repo}/main/web/package.json", as_json=False)
    if not pkg_raw:
        pkg_raw = github_request(f"https://raw.githubusercontent.com/{owner}/{repo}/main/package.json", as_json=False)
    
    if pkg_raw:
        try:
            pkg = json.loads(pkg_raw)
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            if "react" in deps and "React" not in stack:
                stack.append("React")
            elif "vue" in deps and "Vue" not in stack:
                stack.append("Vue")
            elif "svelte" in deps and "Svelte" not in stack:
                stack.append("Svelte")

            if "@mui/material" in deps and "MUI" not in stack and "Material Design 3" not in config.get("preferred_tools", []):
                stack.append("MUI")
        except Exception:
            pass

    # Check pyproject.toml / requirements.txt (Python)
    if not is_rust:
        pyproject_raw = github_request(f"https://raw.githubusercontent.com/{owner}/{repo}/main/pyproject.toml", as_json=False)
        if pyproject_raw:
            if "Python" not in stack:
                stack.insert(0, "Python")
            lower_py = pyproject_raw.lower()
            if "django" in lower_py and "Django" not in stack:
                stack.append("Django")
            if "fastapi" in lower_py and "FastAPI" not in stack:
                stack.append("FastAPI")
            if "scipy" in lower_py and "SciPy" not in stack:
                stack.append("SciPy")
            if "pywebview" in lower_py and "PyWebView" not in stack:
                stack.append("PyWebView")

    # Append preferred specialized tools
    for tool in config.get("preferred_tools", []):
        if tool not in stack:
            stack.append(tool)

    return stack

def format_stack(items):
    return " · ".join(f"`{item}`" for item in items)

def replace_block(content: str, marker_name: str, new_value: str) -> str:
    # Try inline marker format: <!-- auto-sync:marker_name -->...<!-- /auto-sync:marker_name -->
    inline_start = f"<!-- auto-sync:{marker_name} -->"
    inline_end = f"<!-- /auto-sync:{marker_name} -->"
    inline_pattern = re.compile(rf"{re.escape(inline_start)}(.*?){re.escape(inline_end)}", re.DOTALL)
    if inline_pattern.search(content):
        return inline_pattern.sub(f"{inline_start}{new_value}{inline_end}", content)

    # Try block marker format: <!-- auto-sync:marker_name:start -->...<!-- auto-sync:marker_name:end -->
    start_tag = f"<!-- auto-sync:{marker_name}:start -->"
    end_tag = f"<!-- auto-sync:{marker_name}:end -->"
    pattern = re.compile(rf"{re.escape(start_tag)}(.*?){re.escape(end_tag)}", re.DOTALL)
    if pattern.search(content):
        return pattern.sub(f"{start_tag}\n{new_value}\n{end_tag}", content)

    return content

def update_readme():
    readme_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    for name, config in REPO_CONFIG.items():
        owner = config["owner"]
        repo = config["repo"]
        print(f"Processing repository: {owner}/{repo}...")

        # 1. Update version if tracked
        if config.get("version_marker"):
            rel = get_latest_release(owner, repo)
            if rel:
                tag = rel["tag"]
                # Display e.g. "v3.0" from "v3.0.0"
                short_ver = re.sub(r"\.0$", "", tag)
                print(f"  Latest release: {tag} -> {short_ver}")
                content = replace_block(content, config["version_marker"], short_ver)

        # 2. Update stack if tracked
        if config.get("stack_marker"):
            detected_stack = detect_repo_stack(owner, repo, config)
            if detected_stack:
                formatted = format_stack(detected_stack)
                print(f"  Detected stack: {formatted}")
                content = replace_block(content, config["stack_marker"], f"**Stack:** {formatted}")

    if content != original_content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("\nREADME.md updated successfully!")
    else:
        print("\nREADME.md is already up to date.")

if __name__ == "__main__":
    update_readme()
