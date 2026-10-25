from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "teachcloud-flask-api", "version": "1.0.0"})
