"""
Pillar 09: Flask-SQLAlchemy ORM & Flask-Migrate
File: app/models.py
"""

from flask_sqlalchemy import SQLAlchemy\nfrom flask_migrate import Migrate\n\ndb = SQLAlchemy()\nmigrate = Migrate()\n\nclass Article(db.Model):\n    id = db.Column(db.Integer, primary_key=True)\n    title = db.Column(db.String(120), nullable=False)
