from .base import db
from flask_security.models import fsqla_v2 as fsqla


class Role(db.Model, fsqla.FsRoleMixin):
    pass


class User(db.Model, fsqla.FsUserMixin):
    lift_sets = db.relationship("LiftSet", backref=db.backref("user"))
    macro_goals = db.relationship("MacroGoals", backref=db.backref("user"))
    macros_consumed = db.relationship("MacrosConsumed", backref=db.backref("user"))
    vitals = db.relationship("Vitals", backref=db.backref("user"))
