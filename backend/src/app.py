import os
from flask import Flask, render_template_string
from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
)
from .models import db
import logging

log = logging.getLogger("healthdb-backend")
log.setLevel(logging.WARNING)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


def init_app(app, database_path, secret_key, password_salt):
    from . import models, routes

    # options required for the sqlalchemy plugin
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
    # options required for the security plugin
    app.config["SECRET_KEY"] = secret_key
    app.config["SECURITY_PASSWORD_SALT"] = password_salt
    # Allow registration of new users without confirmation
    app.config["SECURITY_REGISTERABLE"] = True
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

    @app.before_first_request
    def init_db():
        db.create_all()

    return app


if __name__ == "__main__":
    app = Flask(__name__)
    init_app(
        app,
        os.environ["DATABASE_FILE_PATH"],
        os.environ["HEALTHDB_SECRET_KEY"],
        os.environ["HEALTHDB_SECURITY_PASSWORD_SALT"],
    )
    app.run(host="0.0.0.0", port=5000)
