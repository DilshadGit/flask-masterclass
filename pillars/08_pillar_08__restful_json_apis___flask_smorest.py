"""
Pillar 08: RESTful JSON APIs & Flask-Smorest
File: api/resources.py
"""

from flask import jsonify, request\n\n@app.route('/api/v1/products', methods=['POST'])\ndef create_product():\n    data = request.get_json()\n    if not data or 'name' not in data:\n        return jsonify({"error": "Validation failed"}), 400\n    return jsonify({"id": 201, "name": data['name']}), 201
