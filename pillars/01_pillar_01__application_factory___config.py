"""
Pillar 01: Application Factory & Config
File: app/__init__.py
"""

from flask import Flask\nfrom config import Config\n\ndef create_app(config_class=Config):\n    app = Flask(__name__)\n    app.config.from_object(config_class)\n    return app
