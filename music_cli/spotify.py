import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def extract_playlist_tracks(playlist_url: str):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
            scope="playlist-read-private playlist-read-collaborative"
        )
    )

    results = sp.playlist_items(playlist_url)
    tracks = []

    while results:
        for item in results["items"]:
            track = item.get("track")
            if track:
                tracks.append({
                    "name": track["name"],
                    "artist": ", ".join(a["name"] for a in track["artists"])
                })

        results = sp.next(results) if results["next"] else None

    return tracks
