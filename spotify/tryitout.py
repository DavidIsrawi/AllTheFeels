# pip install spotipy
import spotipy
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + "Drake", type='artist')
print(results)
