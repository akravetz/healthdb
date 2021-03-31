from .base import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password_hash_salt = db.Column(db.String(200), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), unique=True, nullable=False)

    lift_sets = db.relationship("LiftSet", backref=db.backref("user"))
    macro_goals = db.relationship("MacroGoals", backref=db.backref("user"))
    macros_consumed = db.relationship("MacrosConsumed", backref=db.backref("user"))
