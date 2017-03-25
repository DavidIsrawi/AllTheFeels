from watson_developer_cloud import AlchemyLanguageV1
from watsonCredentials import api_key, url
# Instantiate Watson client
# David's Gmail Extended Account - Trial ends 08/31/2017
alchemy_language = AlchemyLanguageV1(url=url,api_key=api_key)

def getSentiment(text):
    try:
        return alchemy_language.sentiment(text)["docSentiment"]
    except Exception as e:
        print(e)
        raise
