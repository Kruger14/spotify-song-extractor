import os
import subprocess

def download_song(query: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    cmd = [
        "yt-dlp",
        f"ytsearch1:{query}",
        "-x",
        "--audio-format", "mp3",
        "-o", f"{output_dir}/%(title)s.%(ext)s"
    ]

    print(f"🔍 Downloading: {query}")
    try:
        subprocess.run(cmd, check=True)
        print("✔ Done\n")
    except subprocess.CalledProcessError:
        print("❌ Failed\n")
