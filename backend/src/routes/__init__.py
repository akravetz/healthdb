def init_app(app):
    from .test import test_bp

    app.register_blueprint(test_bp)
