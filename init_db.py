from app import app
from models import db

# Import models so Flask knows them
from models.user import User
from models.asset import Asset
from models.ticket import Ticket
from models.vendor import Vendor
from models.document import Document

with app.app_context():
    db.create_all()
    print("Database created successfully!")