from watson_developer_cloud import AlchemyLanguageV1
from watsonCredentials import api_key, url
import json
# Instantiate Watson client
# David's Gmail Extended Account - Trial ends 08/31/2017
alchemy_language = AlchemyLanguageV1(url=url,api_key=api_key)

def getSentiment(text):
    try:
        temp = alchemy_language.sentiment(text)["docSentiment"]
        if(alchemy_language.sentiment(text)["docSentiment"]["type"] == 'neutral'):
            temp["score"] = 0.0
        return temp
    except Exception as e:
        print(e)
        raise