<!--
Note: never start a line with an auto-sync marker, or GitHub renders that line as raw HTML.

Open to (uncomment and edit when needed):
> **Open to:** internships · thesis projects · Rust/Tauri desktop tooling
-->

<h2 align="center">Matteo Benassi</h2>

<p align="center">
  Computer Engineering student at <a href="https://www.unimore.it/">UniMoRe</a>, graduating 2027.<br />
  I build <b>Rust + Tauri</b> desktop apps, self-hosted tools, and hackathon projects that make the podium.
</p>

<p align="center">
  <a href="https://benassimatteo.dev"><img src="https://img.shields.io/badge/benassimatteo.dev-181717?style=flat-square&logo=googlechrome&logoColor=white" alt="Website" /></a>
  <a href="mailto:info@benassimatteo.dev"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <img src="https://img.shields.io/badge/Italy-009246?style=flat-square" alt="Italy" />
  <img src="https://img.shields.io/badge/%F0%9F%A5%87_Hack4Water_2026-B8860B?style=flat-square" alt="Hack4Water 2026 winner" />
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=rust,tauri,ts,react,python,django,postgres,docker&perline=8" alt="Rust, Tauri, TypeScript, React, Python, Django, PostgreSQL, Docker" />
</p>

## Selected work

### 🧪 Oxide

<sub>Desktop app for agentic engineering — co-developed with <a href="https://github.com/cavallinilorenzo">Lorenzo Cavallini</a></sub>

- 🎯 **Problem:** every coding agent lives in its own CLI, with its own workflow.
- 🔨 **Built:** one chat to run coding agents, switching between installed provider CLIs, with Git and GitHub integrations.
- 🧰 **Stack:** `Rust` · `Tauri` · `TypeScript`

[View repository →](https://github.com/cavallinilorenzo/oxide)

### 🎧 scrobbl.rs

<sub>Personal project · self-hosted web app</sub>

- 🎯 **Problem:** Spotify keeps your listening history to itself; I wanted a complete, searchable archive that I own.
- 🔨 **Built:** a single-owner listening archive with owner authentication, background collection of Spotify listens, Spotify extended-history and ListenBrainz imports, rankings, activity charts, searchable history and local AI. Runs locally or with Docker on a persistent data directory.
- 🧰 **Stack:** `Rust` · `React` · `TypeScript` · `SQLite` · `Docker` · `Spotify API`

[View repository →](https://github.com/itsmrma/scrobbl-rs)

### 🎬 SyncForge <sub><!-- auto-sync:syncforge-version -->v3.5.4<!-- /auto-sync:syncforge-version --></sub>

<sub>Personal project · cross-platform desktop app</sub>

- 🎯 **Problem:** syncing audio tracks and subtitles to a different release of the same video by hand is slow and error-prone.
- 🔨 **Built:** 6 modular workflows, including pure-Rust FFT waveform cross-correlation (WaveSync), external & embedded subtitle alignment, lossless remuxing and MKV metadata editing, with batch processing, live logs and standalone releases.
- 🧰 <!-- auto-sync:syncforge-stack -->**Stack:** `JavaScript` · `Rust` · `Tauri v2` · `React` · `MUI` · `FFmpeg` · `MKVToolNix` · `ffsubsync`<!-- /auto-sync:syncforge-stack -->

[View repository →](https://github.com/itsmrma/SyncForge)

## Hackathons

### 🥇 Garda Chiese Alert

<sub>1st place · ACQUAM 2026 · Hack4Water — with <a href="https://github.com/cavallinilorenzo">Lorenzo Cavallini</a> and <a href="https://github.com/TrentoElProgrammatores">Simone Trentin</a></sub>

- 🎯 **Problem:** the Consorzio di bonifica Garda Chiese (33 municipalities, 76,645 ha) needed citizens to report issues on its water network, and operators to know which ones are urgent.
- 🔨 **Built in 3 days:** a no-login web app with GPS, photos and **voice reports parsed by an LLM**. **PostGIS geofencing** rejects reports outside the network before they're sent. Operators triage by danger level on a live map with push notifications.
- 🧰 **Stack:** `Django REST` · `PostgreSQL/PostGIS` · `React` · `TypeScript` · `Leaflet` · `Gemini` · `Docker`

[View repository →](https://github.com/cavallinilorenzo/alert-app-garda-chiese)

### 🥈 Also on the podium

- 🥈 **SCIoTeM 2026** · [Smart Beam](https://github.com/cavallinilorenzo/street-lighting-predictive-maintenance): moves street-lighting maintenance from reactive to predictive with survival analysis + XGBoost and explainable risk scores.
- 🥈 **[SCIoTeM 2025](https://ltomantova.it/2025/02/25/sciotem-2025-smart-city-and-mobility-internet-of-things-digital-twins-and-metaverso/)** · [P7M AI Summarizer](https://github.com/itsmrma/hackathon-p7m-ai-summarizer): strips the PKCS#7 envelope from signed `.p7m` documents and produces AI summaries with page references.

## More projects

- 🎮 **[AMD Fan Control](https://github.com/itsmrma/amd-fan-control)**: AMD GPU fan curves on Windows with telemetry, Zero RPM controls and safe restore.<br><sub>**Stack:** `Rust` · `Tauri` · `TypeScript`</sub>
- 🌀 **[Viessmann Dashboard](https://github.com/itsmrma/viesmann-dashboard-hass)**: Home Assistant add-on combining ViCare entities and direct Viessmann 2701 polling.<br><sub>**Stack:** `Python` · `JavaScript`</sub>
- 🎵 **[Spotify History Analyzer](https://github.com/itsmrma/spotify-history-analyzer)**: private, client-side explorer for Spotify extended history.<br><sub><!-- auto-sync:spotify-stack -->**Stack:** `JavaScript` · `Material Design 3` · `Chart.js` · `JSZip` · `Playwright`<!-- /auto-sync:spotify-stack --></sub>

<details>
<summary><b>University & high school projects</b></summary>
<br />

- 🌿 **[STM32 Smart Garden](https://github.com/itsmrma/STM32CentralinaGettiniWiFI)**: C firmware for weather-aware IoT irrigation on the STM32 B-L475E-IOT01A, with a built-in web server.
- 🎵 **[Music Library](https://github.com/itsmrma/uni-musiclib-project)**: Django platform for music collections with MusicBrainz and TheAudioDB metadata.
- 🗺️ **[Sagre in Lombardia](https://github.com/itsmrma/benpie)**: map-based explorer for Lombardy's local festivals, in PHP.
- 🧩 **[MazeGame](https://github.com/itsmrma/itis-mazegame)**: JavaFX maze game with limited visibility, built in high school.

</details>

## Education

- **B.Sc. Computer Engineering** · UniMoRe, Dipartimento Enzo Ferrari (2027)<br><sub>Now taking: Cyber-Physical Security, Intelligent IoT, Image Processing · all first and second-year exams passed on schedule</sub>
- **Technical high school diploma in computer science** · 100/100

---

<p align="center">
  <sub>Off the keyboard: music (always), motorsport and racing games.</sub>
  <br /><br />
  <a href="https://valid.cpuid.com/hw2uyaqh"><img src="https://valid.cpuid.com/cache/banner/hw2uyaqh.png" alt="CPU-Z Validator" /></a>
</p>
