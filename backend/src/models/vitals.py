from .base import db


class Vitals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # when did this goal start
    effective_date = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    weight_kg = db.Column(db.Integer)
    # stored as 100% = 1, 50% = 0.5, etc
    bodyfat_pct = db.Column(db.Float)
