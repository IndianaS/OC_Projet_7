import requests
from logzero import logger

from settings.settings import key_api_google_back, url_api_google


class ApiGoogle:

    def __init__(self):
        """Initialization url API key api"""

        self.url = url_api_google
        self.key = key_api_google_back

    def api_reading(self, place):
        """Search parameter in the API"""

        params = {
            "address": place,
            "key": key_api_google_back
        }

        response = requests.get(url=url_api_google, params=params)
        data = response.json()
        result_adress = data["results"][0]["formatted_address"]
        result_coordinate = data["results"][0]["geometry"]["location"]
        logger.debug(result_adress)
        logger.debug(result_coordinate)
        return result_adress, result_coordinate
