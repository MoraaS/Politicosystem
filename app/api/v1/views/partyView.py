'''Importing modules and functions to be used and routes relating to parties'''
import re
from flask import Blueprint, make_response, request, jsonify
from app.api.v1.models.partyModel import PartyModel, PARTIES

party_endpoints = Blueprint('party', __name__, url_prefix='/api/v1')


@party_endpoints.route('/parties', methods=['POST'])
def create_party():
    '''Function of creating a party'''
    data = request.get_json()
    try:

        name = data['name']
        hqaddress = data['hqaddress']
        logourl = data['logourl']

        if data['name'].strip() == "":
            return make_response(jsonify({"status": 400,
                                          "error": "Name cant be left blank"}
                                         ), 400)
        if data['hqaddress'].strip() == "":
            return make_response(jsonify({"status": 400,
                                          "error":
                                          "hqaddress cant be blank"}), 400)
        if data['logourl'].strip() == "":
            return make_response(jsonify({"status": 400,
                                          "error":
                                          "logourl cant be blank"}), 400)
        if (len(name) < 6):
            return make_response(jsonify({
                "status": 400,
                "error": "Party name should be more tha 6 characters"
            }), 400)

        if not re.match("^[a-zA-Z]*$", name):
            return make_response(jsonify({
                "status": 400,
                "error": "Party name should only contain alphabets"
            }), 400)

    except:

        return make_response(jsonify({
            "status": 400,
            "error": "You have not provided all the fields"
        }), 400)

    party = PartyModel(name=name,
                       hqaddress=hqaddress, logourl=logourl)
    party.create()

    return make_response(jsonify({
        "status": 201,
        "data": [{"party_id": len(PARTIES), "name": name}]
    }), 201)


@party_endpoints.route('/parties', methods=['GET'])
def get_parties():
    '''Fuction to get all parties'''
    return make_response(jsonify({"status": 200,
                                  "data": PartyModel.get_all()
                                  }), 200)


@party_endpoints.route('/parties/<int:party_id>', methods=['GET'])
def get_single_party(party_id):
    '''Function to get a party using id and
    passing the parameter id to be used'''
    specific_party = PartyModel.get_specific_party(party_id)

    if specific_party:

        return make_response(jsonify({"status": 200,
                                      "data": specific_party}), 200)

    return make_response(jsonify({
        "status": 404,
        "error": "The party does not exist"
    }), 404)


@party_endpoints.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    '''Function to delete party and parameter to be used'''
    deleted_party = PartyModel.delete_party(party_id)
    if deleted_party:
        return make_response(jsonify({
            "status": 200, "data": deleted_party}), 200)
    return make_response(jsonify
                         ({"status": 404, "error":
                           "Could not find this id"}), 404)


@party_endpoints.route('/parties/<int:party_id>/name', methods=['PATCH'])
def update_party(party_id):
    '''Function to update party and parameter to be used'''
    data = request.get_json()
    name = data['name']
    party = PartyModel.edit_party(party_id, name)
    if party:
        return make_response(jsonify({
            "status": 200, "data": party,
            "message": "Party was updated successfully"}), 200)
    else:
        return make_response(jsonify({
            "status": 404, "message": "Could not find this id"}), 404)
