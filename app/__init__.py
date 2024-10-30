from flask import Flask
from app.extension import db
from app.config import DevelopmentConfig
from app.routes.habit import api
from app.routes.habitlog import habitlog
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "TrackIt"})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    app.register_blueprint(api)
    app.register_blueprint(habitlog)

    with app.app_context():
        db.create_all()

    return app