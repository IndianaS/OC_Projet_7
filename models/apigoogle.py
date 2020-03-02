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

        response = requests.get(url=url_api_google, params=params)
        data = response.json()
        result_adress = data["results"][0]["formatted_address"]
        result_coordinate = data["results"][0]["geometry"]["location"]
        logger.debug(result_adress)
        logger.debug(result_coordinate)
        return result_adress, result_coordinate
