from . import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(200))
    file_type = db.Column(db.String(50))  # Invoice / PO / Quotation
    file_path = db.Column(db.String(200))