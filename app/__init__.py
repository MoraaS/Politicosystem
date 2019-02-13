'''Import the Flask class and register blueprints'''
from flask import Flask, make_response, jsonify
from app.api.v1.views.officeView import office_endpoints
from app.api.v1.views.partyView import party_endpoints
from app.api.v2.views.userview import signup
from app.config import app_config


def deal_with_wrong_request(e):
    return make_response(
        jsonify(
            {
                "error": "This is a wrong request",
                "status": 400
            }
        ), 400
    )


def deal_with_wrong_url(e):
    return make_response(
        jsonify(
            {
                "error": "The URL you entered can't be found",
                "status": 400
            }
        ), 400
    )


def deal_with_wrong_method(e):
    return make_response(
        jsonify(
            {
                "error": "Sorry, this is a wrong method",
                "status": 405
            }
        ), 405
    )


# @app.route('/')
# def home():
#     '''Function to initialize the home route'''
#     return "WELCOME TO POLITICO V1"
def create_app(config_name):

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = 'ikeepgoing'

    app.url_map.strict_slashes = False
    app.register_blueprint(office_endpoints)
    app.register_blueprint(party_endpoints)
    app.register_blueprint(signup)
    app.register_error_handler(400, deal_with_wrong_request)
    app.register_error_handler(405, deal_with_wrong_method)
    app.register_error_handler(404, deal_with_wrong_url)

    return app
