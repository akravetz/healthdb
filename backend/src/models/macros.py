
from .base import db


class MacroGoals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # when did this goal start
    effective_start_date = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    # when did it end
    effective_end_date = db.Column(db.DateTime, nullable=True, default=None)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    protein_grams = db.Column(db.Integer, nullable=False)
    carb_grams = db.Column(db.Integer, nullable=False)
    fat_grams = db.Column(db.Integer, nullable=False)


class MacrosConsumed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumed_date = db.Column(db.DateTime, nullable=False)
    added_date = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    protein_grams = db.Column(db.Integer, nullable=False)
    carb_grams = db.Column(db.Integer, nullable=False)
    fat_grams = db.Column(db.Integer, nullable=False)
