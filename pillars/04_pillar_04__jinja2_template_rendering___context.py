"""
Pillar 04: Jinja2 Template Rendering & Context
File: app/templates/index.html
"""

from flask import render_template\n\n@app.route('/dashboard')\ndef dashboard():\n    users = ['Alice', 'Bob', 'Charlie']\n    return render_template('dashboard.html', title='Metrics', users=users)
