from flask import Blueprint, request, jsonify
from models.ticket import Ticket
from models import db

ticket_bp = Blueprint('ticket', __name__)

# GET all tickets
@ticket_bp.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "priority": t.priority,
            "status": t.status
        } for t in tickets
    ])

# CREATE ticket
@ticket_bp.route('/tickets', methods=['POST'])
def add_ticket():
    data = request.json

    ticket = Ticket(
        title=data['title'],
        description=data.get('description', ''),
        priority=data['priority'],
        status="Open"
    )

    db.session.add(ticket)
    db.session.commit()

    return jsonify({"message": "Ticket created successfully"})

# UPDATE status
@ticket_bp.route('/tickets/<int:id>', methods=['PUT'])
def update_ticket(id):
    ticket = Ticket.query.get(id)

    ticket.status = "Closed"
    db.session.commit()

    return jsonify({"message": "Ticket closed"})