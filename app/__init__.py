from flask import Flask
from app.views.redflag import redflag_blueprint

def initialize_app():
    app = Flask(__name__)
    app.register_blueprint(redflag_blueprint, url_prefix='/api/v1')
    return app