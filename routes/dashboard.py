from flask import Blueprint, jsonify
from models.asset import Asset
from models.ticket import Ticket
from models.user import User
from services.monitoring_service import get_system_stats
from services.iot_service import get_environment_data

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard/stats')
def stats():
    return jsonify({
        "assets": Asset.query.count(),
        "tickets_open": Ticket.query.filter_by(status="Open").count(),
        "tickets_closed": Ticket.query.filter_by(status="Closed").count(),
        "users": User.query.count()
    })

@dashboard_bp.route('/dashboard/monitoring')
def monitoring():
    return jsonify(get_system_stats())

@dashboard_bp.route('/dashboard/iot')
def iot():
    return jsonify(get_environment_data())