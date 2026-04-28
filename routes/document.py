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
        file_path = os.path.join(os.getcwd(), doc.file_path)
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
            "id": d.id,
            "name": d.file_name,
            "type": d.file_type,
            "path": d.file_path
        } for d in docs
    ])

# Delete Document
import os

@document_bp.route('/documents/<int:id>', methods=['DELETE'])
def delete_document(id):
    doc = Document.query.get(id)

    if not doc:
        return jsonify({"error": "Not found"}), 404

    # ✅ Debug print (temporary)
    print("Deleting file:", doc.file_path)

    # ✅ Delete file from folder
    if os.path.exists(doc.file_path):
        os.remove(doc.file_path)
        print("File deleted from folder")
    else:
        print("File NOT found in folder")

    # ✅ Delete DB record
    db.session.delete(doc)
    db.session.commit()

    return jsonify({"message": "Document deleted"})