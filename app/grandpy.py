from models.apigoogle import ApiGoogle
from models.apiwiki import ApiWikipedia
from models.parser import Parser


def grandpy(user_text):
    """Application class instance"""

    data = {"status": False}

    parser = Parser(user_text)
    result = parser.clean()

    api_google = ApiGoogle()
    adress, coo = api_google.api_reading(result)

    if adress and coo:
        api_wiki = ApiWikipedia()
        page_id = api_wiki.api_get_page_id(**coo)

        if page_id:
            extract, url = api_wiki.api_get_extract(page_id)
            data = {
                "status": True,
                "question": user_text,
                "article": extract,
                "coords": coo,
                "url": url,
                "adress": adress,
                "response": "Voilà l'endroit demandé mon petit !"
            }

    if not data.get("status"):
        data = {
            "question": user_text,
            "status": False,
            "response": "Je n'ai pas la reponse à la question..!!"
        }

    return data
