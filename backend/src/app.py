import os
from flask import Flask


def create_app():
    from . import models, routes

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_FILE_PATH"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    models.init_app(app)
    routes.init_app(app)
    return app


app = create_app()
