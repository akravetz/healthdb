from .base import db
from .lifts import Lift, LiftSet
from .users import User


def init_app(app):
    db.init_app(app)
