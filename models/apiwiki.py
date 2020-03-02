from pprint import pprint
import logzero
import requests
from logzero import logger

from settings.settings import url_api_wikipedia


class ApiWikipedia:

    def __init__(self):
        self.url = url_api_wikipedia
    
    def api_get_page_id(self, lat, lng):
        """"""
        params = {
            "format": "json", # format de la réponse
            "action": "query", # action à réaliser
            "list": "geosearch", # méthode de recherche
            "gsradius": 100, # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gscoord": f"{lat}|{lng}" # coordonnées GPS séparées par une barre verticale
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
        """"""
        params = {
                "format": "json", # format de la réponse
                "action": "query", # action à effectuer
                "prop": "extracts|info", # Choix des propriétés pour les pages requises
                "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
                "exchars": 2000, # Nombre de caractères à retourner
                "explaintext": 1, # Renvoyer du texte brut (éliminer les balises de markup)
                "pageids": page_id
            }
        response = requests.get(url=url_api_wikipedia, params=params)
        if response.status_code == 200:
            extracts_data = response.json()
            logger.debug("Voici la réponse obtenue: ")
            pprint(extracts_data)
            return extracts_data
        else:
            logger.debug("La requête a donné un status d'erreur")
