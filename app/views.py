from flask import jsonify, render_template, request

from app.grandpy import grandpy
from settings.settings import key_api_google_front

from . import app


@app.route("/")
def home():
    return render_template("index.html", api_key=key_api_google_front)


@app.route("/ajax", methods=["POST"])
def ajax():
    """User text recovery"""

    user_text = request.form["userText"]

    data = grandpy(user_text)

    return jsonify(data)
