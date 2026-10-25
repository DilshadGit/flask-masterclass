# Flask Application Factory Pattern

The Application Factory (`create_app()`) isolates application configuration, enables multi-environment testing, and prevents circular imports:

```python
from flask import Flask
from .extensions import db, login_manager, csrf

def create_app(config_class="config.ProductionConfig") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Register modular blueprints
    from .blueprints.auth import auth_bp
    from .blueprints.api import api_bp
    from .blueprints.main import main_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(api_bp, url_prefix="/api/v1")
    app.register_blueprint(main_bp)

    return app
```
