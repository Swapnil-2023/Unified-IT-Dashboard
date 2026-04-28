from flask import Blueprint, request, jsonify
from models.vendor import Vendor
from models import db

vendor_bp = Blueprint('vendor', __name__)

@vendor_bp.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([
        {
            "id": v.id,
            "name": v.name,
            "contact": v.contact,
            "email": v.email
        } for v in vendors
    ])

@vendor_bp.route('/vendors', methods=['POST'])
def add_vendor():
    data = request.json

    vendor = Vendor(
        name=data['name'],
        contact=data['contact'],
        email=data['email']
    )

    db.session.add(vendor)
    db.session.commit()

    return jsonify({"message": "Vendor added"})

@vendor_bp.route('/vendors/<int:id>', methods=['DELETE'])
def delete_vendor(id):
    vendor = Vendor.query.get(id)

    if not vendor:
        return jsonify({"error": "Vendor not found"}), 404

    db.session.delete(vendor)
    db.session.commit()

    return jsonify({"message": "Vendor deleted"})