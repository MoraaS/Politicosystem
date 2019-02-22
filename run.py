from app import create_app
import os
from flask import make_response, request, jsonify


config_name = os.getenv("APP_SETTINGS")
app = create_app(config_name)


@app.route('/')
def home():
    '''Function to initialize the home route'''
    return "WELCOME TO POLITICO V2"


@app.errorhandler(Exception)
def handle_error(e):
    if request.mimetype != 'application/json':
        return make_response(jsonify({
            "status": 406,
            "message": "data must be of mimetype application/json"
        }), 406)


if __name__ == "__main__":
    app.run(debug=True)
