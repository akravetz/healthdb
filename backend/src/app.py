import os
from flask import Flask


def init_app(app):
    from . import models, routes

    # options required for the sqlalchemy plugin
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_FILE_PATH"]
    # options required for the security plugin
    app.config["SECRET_KEY"] = os.environ.get("HEALTHDB_SECRET_KEY", "")
    app.config["SECURITY_PASSWORD_SALT"] = os.environ.get(
        "HEALTHDB_SECURITY_PASSWORD_SALT", ""
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # As of Flask-SQLAlchemy 2.4.0 it is easy to pass in options directly to the
    # underlying engine. This option makes sure that DB connections from the
    # pool are still valid. Important for entire application since
    # many DBaaS options automatically close idle connections.
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
    }

    models.init_app(app)
    routes.init_app(app)
    return app


if __name__=='__main__':
    app = Flask(__name__)
    init_app(app)
    app.run(host='0.0.0.0', port=5000)
