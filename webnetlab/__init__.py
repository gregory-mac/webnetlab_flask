from flask import Flask, render_template

import config


def error_page_not_found(e):
    return render_template("errors/404.html"), 404


def error_internal_server_error(e):
    return render_template("errors/500.html"), 500


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config)

    with app.app_context():
        from .lab import lab
        from .home import home

        app.register_blueprint(home.home_bp)
        app.register_blueprint(lab.lab_bp, url_prefix="/lab")

        app.register_error_handler(404, error_page_not_found)
        app.register_error_handler(500, error_internal_server_error)

        return app
