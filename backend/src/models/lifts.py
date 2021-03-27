from .base import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password_hash_salt = db.Column(db.String(200), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), unique=True, nullable=False)

    exercise_sets = db.relationship("LiftSet", backref=db.backref("user"))


class Lift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)


class LiftSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    lift_id = db.Column(db.Integer, db.ForeignKey("lift.id"), nullable=False)
    weight_kgs = db.Column(db.Integer, nullable=False)
    rep_count = db.Column(db.Integer, nullable=False)
