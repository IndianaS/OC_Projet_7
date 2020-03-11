from pprint import pprint

import requests
from logzero import logger

from settings.settings import url_api_wikipedia


class ApiWikipedia:
    """Data usage class Api WikiPedia"""

    def __init__(self):
        """Initialization url API"""

        self.url = url_api_wikipedia

    def api_get_page_id(self, lat, lng):
        """Search parameter in the API"""

        params = {
            "format": "json",
            "action": "query",
            "list": "geosearch",
            "gsradius": 100,
            "gscoord": f"{lat}|{lng}"
        }

        response = requests.get(url=url_api_wikipedia, params=params)

        if response.status_code == 200:
            geosearch_data = response.json()

        else:
            geosearch_data = {
                'query': {
                    'geosearch': []
                }
            }
            logger.debug("La requête a donné un status d'erreur")

        page_id = geosearch_data['query']['geosearch'][0]['pageid']
        return page_id

    def api_get_extract(self, page_id):
        """Data extraction from the Wikipedia API"""

        params = {
                "format": "json",
                "action": "query",
                "prop": "extracts|info",
                "inprop": "url",
                "exchars": 2000,
                "explaintext": 1,
                "pageids": page_id
            }
        response = requests.get(url=url_api_wikipedia, params=params)
        if response.status_code == 200:
            extracts_data = response.json()
            logger.debug("Voici la réponse obtenue: ")
            result_extract = extracts_data['query']['pages'][str(page_id)]['extract']
            result_url = extracts_data['query']['pages'][str(page_id)]['canonicalurl']
            logger.debug(result_url)
            pprint(result_extract)
            return result_extract, result_url
        else:
            logger.debug("La requête a donné un status d'erreur")
