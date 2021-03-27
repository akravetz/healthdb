from .base import db
from .lifts import User, Lift, LiftSet


def init_app(app):
    db.init_app(app)
