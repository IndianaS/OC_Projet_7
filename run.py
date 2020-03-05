from models.apigoogle import ApiGoogle
from models.apiwiki import ApiWikipedia
from models.parser import Parser
from logzero import logger


question_utilisateur = "oû se trouve la ville de Grenoble ?"

parser = Parser()
result = parser.clean(question_utilisateur)

api_google = ApiGoogle()
adress, coo = api_google.api_reading(result)

api_wiki = ApiWikipedia()
page_id = api_wiki.api_get_page_id(**coo)
extract = api_wiki.api_get_extract(page_id)
