from flask import Blueprint, request, jsonify
from models.document import Document
from models import db
import os

document_bp = Blueprint('document', __name__)

UPLOAD_FOLDER = 'uploads'

@document_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_type = request.form.get('type')

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        doc = Document(
            file_name=file.filename,
            file_type=file_type,
            file_path=file_path
        )

        db.session.add(doc)
        db.session.commit()

        return jsonify({"message": "File uploaded successfully"})
    
@document_bp.route('/documents', methods=['GET'])
def get_documents():
    docs = Document.query.all()
    return jsonify([
        {
            "name": d.file_name,
            "type": d.file_type,
            "path": d.file_path
        } for d in docs
    ])