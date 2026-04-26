from . import db

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    status = db.Column(db.String(50))
    assigned_user_id = db.Column(db.Integer)