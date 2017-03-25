# All the Feels
------------
## Project Idea
Alexa: How’s your day going?
User: Some response of day went.

System processes this response, analyzes your response and plays a song corresponding to that mood

## What we need/what we will use:

Amazon Echo Integration
Spotify API to play playlist : https://developer.spotify.com/web-api/playlist-endpoints/
Watson analyze emotion of response (day)

## Architecture
- [ ] Alexa -> JSON -> Text from user
- [X] Text from user -> Python -> Watson score
- [ ] Score -> Python code -> playlist id (closest score)
- [ ] Playlist id -> spotify api -> play on alexa
