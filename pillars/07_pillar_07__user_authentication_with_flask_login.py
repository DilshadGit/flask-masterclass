"""
Pillar 07: User Authentication with Flask-Login
File: app/models.py & routes.py
"""

from flask_login import login_user, login_required, UserMixin\nfrom werkzeug.security import generate_password_hash, check_password_hash\n\nhash_pw = generate_password_hash("SuperSecret123")\nis_valid = check_password_hash(hash_pw, "SuperSecret123")
