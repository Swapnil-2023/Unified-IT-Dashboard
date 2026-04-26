from flask import render_template
from flask import Flask
from config import Config
from models import db
from routes.dashboard import dashboard_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(dashboard_bp)

db.init_app(app)

@app.route("/")
def home():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)