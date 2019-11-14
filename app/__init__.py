from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from . import api
        app.register_blueprint(api.bp)
        register_error_handlers(app)
        return app


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        error_msg = str(error)
        response = {"messages": error_msg}
        return jsonify(response), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        error_msg = str(error)
        response = {"messages": error_msg}
        return jsonify(response), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        # Hide the "error" from the visitor. It can be stored to a file/db/service to log and identify the issue
        error_msg = "Something went wrong"
        response = {"messages": error_msg}
        return jsonify(response), 500

    @app.errorhandler(Exception)
    def unhandled_exception(ex):
        # Hide the "ex" from the visitor. It can be stored to a file/db/service to log and identify the issue
        error_msg = "Something went wrong"
        response = {"messages": error_msg}
        return jsonify(response), 500
