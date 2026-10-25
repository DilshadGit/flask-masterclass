"""
Pillar 03: Modular Architecture with Blueprints
File: auth/routes.py
"""

from flask import Blueprint, jsonify\n\nauth_bp = Blueprint('auth', __name__, url_prefix='/auth')\n\n@auth_bp.route('/login', methods=['POST'])\ndef login():\n    return jsonify({"status": "authenticated"}), 200
