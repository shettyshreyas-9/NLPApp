import pandas

import os
import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key('VYHSNYk4wCdXfMIYEnNUc3sq6oNDI9Tyg2Db4HSEblE')

    # sentiment analysis
    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    # named entity recognition
    def named_entity_recognition(self,text):
        response = paralleldots.ner(text)
        return response


