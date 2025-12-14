# 🎵 Spotify Music CLI Downloader

A **production-ready Python CLI tool** to download songs and playlists as MP3 using `yt-dlp`.

Supports:

* ✅ Single song download by name
* ✅ Spotify playlist → download
* ✅ Download directly from a playlist **JSON file** (no Spotify link needed)
* ✅ `.env`-based configuration
* ✅ Clean, extensible architecture

---

## 📁 Project Structure

```
music_cli/
│
├── music_cli/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── downloader.py       # yt-dlp logic
│   └── spotify.py          # Spotify playlist extraction
│
├── downloads/              # Downloaded MP3 files
├── data/                   # (Optional) playlist JSON files
│   └── playlist.json
│
├── .env                    # Spotify credentials
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

* Python **3.9+**
* `ffmpeg` installed and available in PATH
* `yt-dlp` installed via pip

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd music_cli
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration (`.env`)

Create a `.env` file in the project root:

```env
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8080
```

🔹 Required **only** for Spotify playlist extraction
🔹 Not required for JSON or single-song downloads

---

## 🚀 Usage

All commands are run from the **project root**.

```bash
python -m music_cli.cli <command> [options]
```

---

## 🎵 Download a Single Song

Download one song by name.

```bash
python -m music_cli.cli song "Believer Imagine Dragons"
```

Custom output folder:

```bash
python -m music_cli.cli song "Blinding Lights The Weeknd" -o downloads
```

---

## 🎶 Download a Spotify Playlist

Download all songs from a Spotify playlist URL.

```bash
python -m music_cli.cli playlist https://open.spotify.com/playlist/XXXXXXXX
```

Save extracted playlist as JSON:

```bash
python -m music_cli.cli playlist https://open.spotify.com/playlist/XXXXXXXX --json playlist.json
```

Custom output folder:

```bash
python -m music_cli.cli playlist URL -o my_music
```

---

## 📄 Download from a JSON Playlist (NO Spotify)

If you already have a playlist JSON file:

```json
[
  { "name": "Believer", "artist": "Imagine Dragons" },
  { "name": "Blinding Lights", "artist": "The Weeknd" }
]
```

Download directly:

```bash
python -m music_cli.cli json playlist.json
```

From a folder:

```bash
python -m music_cli.cli json data/playlist.json -o downloads
```

✔ No Spotify
✔ No internet auth

---

## 📍 Where to Place JSON Files

Recommended locations:

* Project root: `playlist.json`
* Dedicated folder: `data/playlist.json`
* Anywhere on system (use full path)

Example:

```bash
python -m music_cli.cli json "C:\Users\You\Music\playlist.json"
```

---

## 🧠 Workflow Examples

### Spotify → JSON → Download

```bash
python -m music_cli.cli playlist URL --json playlist.json
python -m music_cli.cli json playlist.json
```

---

## 🛠 How It Works

1. **Spotify mode**

   * Extracts song metadata using Spotify API
2. **JSON mode**

   * Reads song names & artists from file
3. **Downloader**

   * Uses `yt-dlp` search
   * Extracts best audio
   * Converts to MP3

---

## ⚠️ Notes & Best Practices

* Use `.env` for secrets (never commit it)
* JSON mode is fastest & most reliable
* Spotify mode may be rate-limited

---

## 🔮 Future Extensions

I am planning to extend this tool into:

* FastAPI / Django REST backend
* Flutter / React frontend integration
* Parallel downloads
* Resume & retry
* Global CLI command (`music download ...`)

---

## 🧪 Help & Debugging

Show help:

```bash
python -m music_cli.cli --help
```

Command help:

```bash
python -m music_cli.cli json --help
```

---

## ⚖️ Disclaimer

This tool is for **educational and personal use only**.
Respect content creators and platform terms of service.

---
