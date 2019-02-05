
from flask import Flask
from app.api.v1.views.officeView import office_endpoints
from app.api.v1.views.partyView import party_endpoints


app = Flask(__name__)

app.register_blueprint(office_endpoints)
app.register_blueprint(party_endpoints)
