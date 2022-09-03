from flask import Flask

import config


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config)

    with app.app_context():
        from .lab import lab
        from .home import home

        app.register_blueprint(home.home_bp)
        app.register_blueprint(lab.lab_bp)

        return app
