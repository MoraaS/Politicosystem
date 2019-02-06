from flask import Flask, Blueprint, make_response, request, jsonify
from app.api.v1.models.partyModel import partyModel

party_endpoints = Blueprint('party', __name__, url_prefix='/api/v1')


@party_endpoints.route('/parties', methods=['POST'])
def create_party():
    data = request.get_json()
    try:

        party_id = data['party_id']
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']

    except:

        return make_response(jsonify({
            "status": 400,
            "error": "You have not provided all the fields"
        }), 400)

    party = partyModel(party_id=party_id, name=name,
                       hqAddress=hqAddress, logoUrl=logoUrl)
    party.create()

    return make_response(jsonify({
        "status": 201,
        "data": [{"party_id": party_id, "name": name}]
    }), 201)


@party_endpoints.route('/parties', methods=['GET'])
def get_offices():
    return make_response(jsonify({"status": 200,
                                  "data": partyModel.get_all()
                                  }), 200)


@party_endpoints.route('/parties/<int:party_id>', methods=['GET'])
def get_single_party(party_id):
    specific_party = partyModel.get_specific_party(party_id)

    if specific_party:

        return make_response(jsonify({"status": 200,
                                      "data": specific_party}), 200)

    return make_response(jsonify({
        "status": 404,
        "error": "The party does not exist"
    }), 404)


@party_endpoints.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    deleted_party = partyModel.delete_party(party_id)
    if deleted_party:
        return make_response(jsonify({
            "status": 200, "data": deleted_party}), 200)
    return make_response(jsonify({"status": 404, "message": "Party successfully deleted",
                                  "error": "Could not find this id"}), 404)
