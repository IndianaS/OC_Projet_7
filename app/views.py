import logzero
from flask import jsonify, render_template, request
from logzero import logger

from . import app


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]
    logger.debug(user_text)
    return jsonify(["pas de réponse"])
