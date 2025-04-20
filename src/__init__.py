import logging
from flask import Flask, jsonify, request
from flask_httpauth import HTTPTokenAuth
from flask_migrate import Migrate # noqa: F401
from src.utils.init_logger import init_logger
from src.utils.common import retrieve_secret
from src.env_config import EnvConfig
from src.constants import Constant
from src.extensions import db, migrate
from dotenv import load_dotenv
from src.error_handlers import register_error_handlers

load_dotenv()
init_logger()

auth = HTTPTokenAuth(header="X-api-key")

API_PREFIX = "/api/v1"
API_PREFIX_HEALTH = "health"
API_PREFIX_CASES = "cases"

logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(EnvConfig)

    # Import models here to ensure they are registered with SQLAlchemy
    from src import models  # noqa: F401
    from src.routes.case_route import case_bp
    from src.routes.health_route import health_bp

    app.register_blueprint(health_bp, url_prefix=f"{API_PREFIX}/{API_PREFIX_HEALTH}")
    app.register_blueprint(case_bp, url_prefix=f"{API_PREFIX}/{API_PREFIX_CASES}")

    db.init_app(app)
    migrate.init_app(app, db)

    register_error_handlers(app)

    @auth.verify_token
    def verify_token(token):
        if token == retrieve_secret(Constant.SecretKeys.THIRD_PARTY_API_KEY.value):
            return "authenticated"

    @app.before_request
    def check_auth_exclusions():
        if request.path == f"{API_PREFIX}/{API_PREFIX_HEALTH}":
            return None

    @auth.error_handler
    def auth_error(status):
        return jsonify({"message": "Access denied: Invalid or expired token."}), status

    # @app.route("/")
    # @auth.login_required
    # def hello_world():
    #     return "Hello this is evaluation app!"

    # @app.route('/cases', methods=['GET'])
    # @auth.login_required
    # def trigger_tickets_robots():
    #     if request.method == 'GET':
    #         args = request.args
    #         return trigger_tickets_robots_group_id(int(args.get("bau_group_id")), args.get("view_id"))
    #     return "Invalid method", 400

    return app
