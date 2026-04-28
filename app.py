from flask import render_template
from flask import Flask
from config import Config
from models import db
from routes.dashboard import dashboard_bp
from routes.asset import asset_bp
from routes.ticket import ticket_bp
from routes.vendor import vendor_bp
from routes.document import document_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(dashboard_bp)
app.register_blueprint(asset_bp)
app.register_blueprint(ticket_bp)
app.register_blueprint(vendor_bp)
app.register_blueprint(document_bp)

db.init_app(app)

@app.route("/")
def home():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)