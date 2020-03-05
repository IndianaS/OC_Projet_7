import logzero
from flask import jsonify, render_template, request
from logzero import logger
from models.apigoogle import ApiGoogle
from models.apiwiki import ApiWikipedia
from models.parser import Parser

from . import app

#question_utilisateur = "Salut Grandpy, comment vas-tu? avez-vous passé une bonne soirée avec mémé hier soir? au fait, pourrais-tu m'indiquer ou se trouve le Musée du Louvre?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]

    logger.debug("Question posée :" + user_text)

    parser = Parser()
    result = parser.clean(user_text)

    api_google = ApiGoogle()
    adress, coo = api_google.api_reading(result)

    api_wiki = ApiWikipedia()
    page_id = api_wiki.api_get_page_id(**coo)
    extract, url = api_wiki.api_get_extract(page_id)

    data = { 
        "question" : user_text,
        "article" : extract,
        "coords" : coo,
        "url" : url,
        "adress" : adress
    }

    return jsonify(data)
