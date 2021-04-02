import csv
import os.path
from pathlib import Path
from flask import Flask
from src.app import init_app
from src.models import db, user_store, Lift

SEEDER_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def seed_func(db, filename, func):
    with open(f"{SEEDER_DIRECTORY}/{filename}", "r", newline="") as f:
        rdr = csv.DictReader(f, delimiter="\t")
        for row in rdr:
            func(row)
    db.session.commit()


def seed_admins(db, filename):
    seed_func(
        db,
        filename,
        lambda row: user_store.create_user(
            email=row["username"], password=row["password_hash"]
        ),
    )


def seed_class(db, filename, cls):
    seed_func(db, filename, lambda row: db.session.add(cls(**row)))


def main():
    core = os.environ["CORE"]
    db_path = os.path.join(core, "backend/database.db")
    os.environ["DATABASE_FILE_PATH"] = f"/{db_path}"

    app = Flask(__name__)
    app.app_context().push()

    init_app(app)
    db.create_all()

    print("seeding admin users")
    seed_admins(db, "users.tsv")
    print("seeding lifts")
    seed_class(db, "lifts.tsv", Lift)


if __name__ == "__main__":
    main()
