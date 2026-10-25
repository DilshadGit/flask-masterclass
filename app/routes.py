from flask import Blueprint, jsonify, request
from app.models import Note, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return jsonify({"status": "online", "framework": "Flask 3.0", "author": "DilshadGit"})

@main_bp.route('/api/notes', methods=['GET', 'POST'])
def handle_notes():
    if request.method == 'POST':
        data = request.get_json() or {}
        note = Note(title=data.get('title', 'Untitled'), body=data.get('body', ''))
        db.session.add(note)
        db.session.commit()
        return jsonify({"success": True, "id": note.id}), 201

    notes = Note.query.all()
    return jsonify([{"id": n.id, "title": n.title, "body": n.body} for n in notes])
