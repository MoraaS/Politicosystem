'''Import the Flask class and register blueprints'''
from flask import Flask
from app.api.v1.views.officeView import office_endpoints
from app.api.v1.views.partyView import party_endpoints


app = Flask(__name__)


@app.route('/')
def home():
    '''Function to initialize the home route'''
    return "WELCOME TO POLITICO V1"

app.url_map.strict_slashes = False
app.register_blueprint(office_endpoints)
app.register_blueprint(party_endpoints)
