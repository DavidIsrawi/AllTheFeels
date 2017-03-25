from watsonAlchemy import getSentiment
import json

with open('../spotify/playlists.json') as data:
    playlists = json.load(data)

def findPlaylist(score):
    for playlist in playlists:
        playlist["dif"] = abs(score - playlist["emotion"])

    playlists = sorted(playlists, key=lambda x : x["dif"], reverse=False)
    # for playlist in playlists:
    #     print(playlist)
