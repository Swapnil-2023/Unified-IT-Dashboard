from app import app
from models import db

# Import models so Flask knows them
from models.user import User
from models.asset import Asset
from models.ticket import Ticket
from models.vendor import Vendor
from models.document import Document

with app.app_context():

    # Create all tables
    db.create_all()

    # Create default admin user
    admin = User.query.filter_by(
        email='admin@dashboard.local'
    ).first()

    if not admin:

        admin = User(
            name='Admin',
            email='admin@dashboard.local',
            password='admin123',
            role='Admin'
        )

        db.session.add(admin)
        db.session.commit()

        print("Default admin user created!")

    print("Database created successfully!")