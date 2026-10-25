from flask import Flask
from .extensions import db, login_manager, csrf

def create_app(config_object="config.Config") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    login_manager.login_view = 'auth.login'

    from .blueprints.auth import auth_bp
    from .blueprints.api import api_bp
    from .blueprints.main import main_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
