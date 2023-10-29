import pandas

import os
import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key('VYHSNYk4wCdXfMIYEnNUc3sq6oNDI9Tyg2Db4HSEblE')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response


