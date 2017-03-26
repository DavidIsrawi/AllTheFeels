import json

# global playlists
#
# with open('playlists.json') as data:
#     playlists = json.load(data)

def findPlaylist(score):
    with open('playlists.json') as data:
        playlists = json.load(data)
    for playlist in playlists:
        playlist["dif"] = abs(score - playlist["emotion"])

    playlists = sorted(playlists, key=lambda x : x["dif"], reverse=False)
    return playlists
    # for playlist in playlists:
    #     print(playlist)

# print findPlaylist(-0.1349234)
# answer = (-0.125324234)
# print str(round(answer, 2))