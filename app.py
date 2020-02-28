from models.apigoogle import ApiGoogle
from models.parser import Parser

question_utilisateur = "Salut Grandpy, comment vas-tu? avez-vous passé une bonne soirée avec mémé hier soir? au fait, pourrais-tu m'indiquer ou se trouve le musée su Louvre?"

parser = Parser()
result = parser.clean(question_utilisateur)

api_google = ApiGoogle()
api_google.api_reading(result)
