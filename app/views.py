from flask import jsonify, render_template, request
from logzero import logger
from models.apigoogle import ApiGoogle
from models.apiwiki import ApiWikipedia
from models.parser import Parser
from settings.settings import key_api_google_front

from . import app


@app.route("/")
def home():
    """"""
    return render_template("index.html", api_key=key_api_google_front)


@app.route("/ajax", methods=["POST"])
def ajax():
    """"""
    user_text = request.form["userText"]

    logger.debug("Question posée :" + user_text)

    parser = Parser(user_text)
    result = parser.clean()

    api_google = ApiGoogle()
    adress, coo = api_google.api_reading(result)

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
    else:
        data = {
            "question": user_text,
            "status": False,
            "response": "La recherche concerne aucun lieu...!"
        }

    return jsonify(data)
