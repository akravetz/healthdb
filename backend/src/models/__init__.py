from .base import db
from .lifts import Lift, LiftSet
from .macros import MacroGoals, MacrosConsumed
from .vitals import Vitals
from .users import User, Role
from flask_security.models import fsqla_v2 as fsqla
from flask_security import Security, SQLAlchemyUserDatastore

user_store = SQLAlchemyUserDatastore(db, User, Role)


def init_app(app):
    db.init_app(app)
    # initialize authentication

    security = Security(app, user_store)
