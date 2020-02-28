import requests
from settings.settings import url_api_google, key_api_google
import logzero
from logzero import logger

class ApiGoogle:

    def __init__(self):
        self.url = url_api_google
        self.key = key_api_google
    
    def api_reading(self, place):
        params = {
            "address": place,
            "key": key_api_google
        }

        response = requests.get(url_api_google, params=params)
        data = response.json()
        logger.debug(data["results"][0]["formatted_address"])
        return data["results"][0]["formatted_address"]
