
from flask import Flask
from app.api.v1.views.officeView import office_endpoints



app = Flask(__name__)

app.register_blueprint(office_endpoints)