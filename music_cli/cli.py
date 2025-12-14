import argparse
import json
import sys
from dotenv import load_dotenv

from music_cli.downloader import download_song
from music_cli.spotify import extract_playlist_tracks

# Load environment variables from .env
load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        description="🎵 Music CLI Downloader"
    )

    subparsers = parser.add_subparsers(dest="command")

    # =========================
    #  SINGLE SONG COMMAND
    song_parser = subparsers.add_parser(
        "song",
        help="Download a single song by name"
    )
    song_parser.add_argument(
        "name",
        help="Song name (e.g. 'Believer Imagine Dragons')"
    )
    song_parser.add_argument(
        "-o", "--out",
        default="downloads",
        help="Output directory"
    )

    # =========================
    #  SPOTIFY PLAYLIST COMMAND
    playlist_parser = subparsers.add_parser(
        "playlist",
        help="Download songs from a Spotify playlist URL"
    )
    playlist_parser.add_argument(
        "url",
        help="Spotify playlist URL"
    )
    playlist_parser.add_argument(
        "-o", "--out",
        default="downloads",
        help="Output directory"
    )
    playlist_parser.add_argument(
        "--json",
        help="Save extracted playlist as JSON file"
    )

    # =========================
    #  JSON PLAYLIST COMMAND
    json_parser = subparsers.add_parser(
        "json",
        help="Download songs from a playlist JSON file"
    )
    json_parser.add_argument(
        "file",
        help="Path to playlist JSON file"
    )
    json_parser.add_argument(
        "-o", "--out",
        default="downloads",
        help="Output directory"
    )

    args = parser.parse_args()

    # =========================
    #  COMMAND HANDLING
    if args.command == "song":
        query = f"{args.name} audio"
        download_song(query, args.out)

    elif args.command == "playlist":
        try:
            tracks = extract_playlist_tracks(args.url)
        except Exception as e:
            print(f"❌ Spotify error: {e}")
            sys.exit(1)

        if args.json:
            with open(args.json, "w", encoding="utf-8") as f:
                json.dump(tracks, f, indent=2, ensure_ascii=False)

        print(f"🎶 Found {len(tracks)} tracks\n")

        for track in tracks:
            query = f"{track['name']} {track['artist']} audio"
            download_song(query, args.out)

    elif args.command == "json":
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                tracks = json.load(f)
        except Exception as e:
            print(f"❌ Failed to read JSON file: {e}")
            sys.exit(1)

        if not isinstance(tracks, list):
            print("❌ Invalid JSON format (expected a list of songs)")
            sys.exit(1)

        print(f"🎶 Found {len(tracks)} tracks\n")

        for track in tracks:
            if "name" not in track or "artist" not in track:
                print("⚠ Skipping invalid entry:", track)
                continue

            query = f"{track['name']} {track['artist']} audio"
            download_song(query, args.out)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
