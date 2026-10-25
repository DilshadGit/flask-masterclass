"""
Pillar 06: Client-Side Cryptographic Sessions
File: app/routes.py
"""

from flask import session, redirect, url_for\n\n@app.route('/set-session')\ndef set_session():\n    session['user_id'] = 101\n    session['logged_in'] = True\n    return jsonify({"session_status": "set"})
