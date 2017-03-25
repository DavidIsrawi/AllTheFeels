# All the Feels

## Project Idea
- Alexa: How’s your day going?
- User: (explains day)
- Alexa: I feel you. I found some good playlists for you to listen to. Would you like to listen to X?
- User: Yes
- Alexa: (Play from Spotify)

### Optional 1
- User: No
- Alexa: Ok. What about the Y playlist?

### Optional 2
- User: I don't want to listen to music
- Alexa: Alright

## What we need/what we will use:

- Amazon Echo Integration (https://developer.amazon.com/alexa-skills-kit)
- Watson AlchemyAPI (https://www.ibm.com/watson/developercloud/alchemy-language.html)

## Architecture
- [ ] Alexa -> JSON -> Text from user
- [X] Text from user -> Python -> Watson score
- [ ] Score -> Python code -> Playlist
- [ ] Playlist -> Play through Alexa
