import spotipy
from spotipy.oauth2 import SpotifyOAuth

def select_songs(mood, language):
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    playlists = sp.current_user_playlists()
    songs = []
    for playlist in playlists['items']:
        tracks = sp.playlist_tracks(playlist['id'])
        for track in tracks['items']:
            if (mood in track['name'].lower() or mood in track['artists'][0]['name'].lower()) and language in track['name'].lower():
                songs.append(track['uri'])
    return songs

mood = input("What mood are you in? ")
language = input("What language do you prefer? ")
songs = select_songs(mood, language)
print(f"Here are some songs for your {mood} mood and in {language}:")
for song in songs:
    print(song)
