import csv
import os.path
from pathlib import Path
from flask import Flask
from models import db, User, Lift, init_app


def seed(db, cls, filename):
    with open(filename, "r", newline="") as f:
        rdr = csv.DictReader(f, delimiter="\t")
        for row in rdr:
            res = cls(**row)
            db.session.add(res)
    db.session.commit()


def main():
    core = os.environ['CORE']
    db_path = os.path.join(core, 'backend/database.db')
    
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.app_context().push()

    init_app(app)
    db.create_all()

    seed(db, User, "users.tsv")
    seed(db, Lift, "lifts.tsv")


if __name__ == "__main__":
    main()
