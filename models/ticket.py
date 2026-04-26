from . import db

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    priority = db.Column(db.String(20))
    status = db.Column(db.String(20))
    assigned_to = db.Column(db.Integer)