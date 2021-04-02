import os
from flask import Flask
from .app import init_app

app = Flask(__name__)
init_app(
    app,
    os.environ["DATABASE_FILE_PATH"],
    os.environ["HEALTHDB_SECRET_KEY"],
    os.environ["HEALTHDB_SECURITY_PASSWORD_SALT"],
)
