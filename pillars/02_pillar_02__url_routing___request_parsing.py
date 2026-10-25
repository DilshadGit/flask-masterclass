"""
Pillar 02: URL Routing & Request Parsing
File: app/routes.py
"""

from flask import jsonify, request\nfrom app import app\n\n@app.route('/api/users/<int:user_id>', methods=['GET'])\ndef get_user(user_id):\n    role = request.args.get('role', 'Developer')\n    return jsonify({"user_id": user_id, "role": role}), 200
