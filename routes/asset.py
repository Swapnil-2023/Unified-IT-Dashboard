from flask import Blueprint, request, jsonify
from models.asset import Asset
from models import db
from models.user import User
from models.vendor import Vendor

asset_bp = Blueprint('asset', __name__)

# GET all assets
@asset_bp.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([
    {
        "id": a.id,
        "name": a.name,
        "type": a.type,
        "status": a.status,
        "user": User.query.get(a.assigned_user_id).name if a.assigned_user_id else "Unassigned",
        "vendor": Vendor.query.get(a.vendor_id).name if a.vendor_id else "No Vendor"
    }
    for a in assets
])

# ADD asset
@asset_bp.route('/assets', methods=['POST'])
def add_asset():
    data = request.json

    asset = Asset(
        name=data['name'],
        type=data['type'],
        status="Active",
        assigned_user_id=data.get('assigned_user_id'),
        vendor_id=data.get('vendor_id')
    )

    db.session.add(asset)
    db.session.commit()

    return jsonify({"message": "Asset added successfully"})

# Delete asset
@asset_bp.route('/assets/<int:id>', methods=['DELETE'])
def delete_asset(id):
    asset = Asset.query.get(id)

    db.session.delete(asset)
    db.session.commit()

    return jsonify({"message": "Asset deleted"})
