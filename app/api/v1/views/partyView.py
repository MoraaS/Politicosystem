from flask import Flask, Blueprint, make_response, request, jsonify
from app.api.v1.models.partyModel import partyModel

party_endpoints=Blueprint('party',__name__,url_prefix='/api/v1')

@party_endpoints.route('/parties', methods=['POST'])
def create_party():
    data = request.get_json()
    try:

        party_id= data['party_id']
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl=data['logoUrl']

    except:

        return make_response(jsonify({
            "status": 400,
            "error": "You have not provided all the fields"
        }), 400)

    party = partyModel(party_id=party_id, name=name,
                         hqAddress=hqAddress,logoUrl=logoUrl)
    party.create()

    return make_response(jsonify({
        "status": 201,
        "data": [{"party_id": party_id, "name": name}]
    }), 201)