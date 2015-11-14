from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request,url_for, flash, session, jsonify,abort
from flask_debugtoolbar import DebugToolbarExtension
import os


SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")

app = Flask(__name__)

app.secret_key = SECRET_KEY


app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""


    return render_template("index.html")



if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    # DebugToolbarExtension(app)


    
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
    # app.run()
