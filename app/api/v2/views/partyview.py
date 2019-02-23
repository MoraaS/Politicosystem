import re
from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.partymodel import PartyModel
from app.api.utils import validate_parties
import json
from app.api.utils import admin_required

party_v2 = Blueprint('party2', __name__, url_prefix='/api/v2/')


@party_v2.route('/parties', methods=['POST'])
@admin_required
def create_party():
    '''Function of creating a party'''
    errors = validate_parties(request)
    if not errors:

        data = request.get_json()
        name = data['name']
        hqaddress = data['hqaddress']
        logourl = data['logourl']

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

        party = PartyModel()

        if party.get_party_by_name(name):
            return make_response(jsonify({"error": "The Party Name Already exists",
                                          "status": 400}), 400)
        party.create(name, hqaddress, logourl)
        party_object = []
        party = {
            "name": name,
            "hqaddress": hqaddress,
            "logourl": logourl
        }
        party_object.append(party)
        return make_response(jsonify({
            "status": 201,
            "message": "party created successfully"
        },
            party_object
        ), 201)

    else:
        return make_response(jsonify({"errors": errors,
                                      "status": 400}), 400)


@party_v2.route('/parties', methods=['GET'])
def get_parties():
    '''Fuction to get all parties'''
    return make_response(jsonify({"status": 200,
                                  "parties": json.loads(PartyModel().get_all_parties())
                                  }), 200)


@party_v2.route('/parties/<int:party_id>', methods=['GET'])
def get_single_party(party_id):
    '''Function to get a party using id and
    passing the parameter id to be used'''
    specific_party = PartyModel().get_party_by_id(party_id)
    specific_party = json.loads(specific_party)

    if specific_party:

        return make_response(jsonify({"status": 200,
                                      "data": specific_party}), 200)

    return make_response(jsonify({
        "status": 404,
        "error": "The party does not exist"
    }), 404)


@party_v2.route('/parties/<int:party_id>', methods=['DELETE'])
@admin_required
def delete_party(party_id):
    '''Function to delete party and parameter to be used'''
    deleted_party = PartyModel().get_party_by_id(party_id)
    if deleted_party:
        PartyModel().delete_party(party_id)
        return make_response(jsonify({"message": "The party has been deleted"}), 200)
    return make_response(jsonify({"message": "party not found"}), 200)


@party_v2.route('/parties/<int:party_id>/edit', methods=['PUT'])
@admin_required
def edit_party(party_id):
    '''Function to edit parties'''
    errors = validate_parties(request)
    if not errors:

        data = request.get_json()
        name = data['name']
        hqaddress = data['hqaddress']
        logourl = data['logourl']
        p = PartyModel().get_party_by_id(party_id)
        print(p)
        if p:
            party = PartiesModel().update_party(name, hqaddress, logourl, party_id)
            return make_response(jsonify({"message": "The party has been updated successfully"}), 200)
        return make_response(jsonify({"error": "The party could not be found"}), 404)

    else:
        return make_response(jsonify({"errors": errors,
                                      "status": 400}), 400)
