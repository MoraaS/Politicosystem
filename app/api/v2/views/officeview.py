import re
from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.officemodel import OfficeModel
import json
from app.api.utils import login_required, admin_required, validate_office
from app.api.v2.models.usermodel import UserModel
from app.api.v2.models.candidates import CandidatesModel

office_v2 = Blueprint('office2', __name__, url_prefix='/api/v2/')


@office_v2.route('/offices', methods=['POST'])
@admin_required
def create_office():
    '''Function to create a new office'''
    errors = validate_office(request)
    if not errors:

        data = request.get_json()
        name = data['name']
        office_type = data['office_type']

        if (len(name) < 6):
            return make_response(jsonify({
                "status": 400,
                "error": "Name cannot be less than 6 characters"
            }), 400)
        if not re.match("^[a-zA-Z]*$", name):
            return make_response(jsonify({
                "status": 400,
                "error": "Office name should only contain alphabets"
            }), 400)

        office = OfficeModel()

        if office.get_office_by_name(name):
            return make_response(jsonify({"error": "The Office Name Already exists",
                                          "status": 400}), 400)
        office.create(name, office_type)

        office_object = []
        office = {
            "name": name,
            "office_type": office_type
        }
        office_object.append(office)
        return make_response(jsonify({
            "status": 201,
            "message": "office created successfully"
        },
            office_object
        ), 201)

    else:
        return make_response(jsonify({"errors": errors,
                                      "status": 400

                                      }), 400)


@office_v2.route('/offices', methods=['GET'])
def get_offices():
    '''Function to get all offices'''
    return make_response(jsonify({"status": 200,
                                  "offices": json.loads(OfficeModel()
                                                        .get_all_offices())}), 200)


@office_v2.route('/offices/<int:office_id>', methods=['GET'])
def get_by_id(office_id):
    '''Function to get office by id and passing the parameter id'''
    specific_office = OfficeModel().get_by_id(office_id)
    specific_office = json.loads(specific_office)

    if specific_office:

        return make_response(jsonify({"status": 200,
                                      "data": specific_office}), 200)

    return make_response(jsonify({
        "status": 404,
        "error": "The office does not exist"
    }), 404)


@office_v2.route('/offices/<int:office_id>/register', methods=['POST'])
@admin_required
def register_candidate(office_id):
    '''Function to register candidate passing the parameter id'''
    specific_office = OfficeModel().get_by_id(office_id)

    if specific_office == 'null':
        return make_response(jsonify({
            "status": 404,
            "error": "The office does not exist"
        }), 404)

    data = request.get_json()
    party_id = data['party_id']
    candidate_id = data['candidate_id']

    user = UserModel()
    user_id = user.get_user_by_id(candidate_id)
    print(user_id)

    if not user_id:
        return make_response(jsonify({
            "status": 404,
            "error": "The user does not exist"
        }), 404)

    check_cand = CandidatesModel().get_by_id(candidate_id)

    if check_cand:
        return make_response(jsonify({
            "status": 400,
            "error": "The candidate already exists"
        }), 400)
    else:
        new_cand = CandidatesModel().create(office_id, party_id, candidate_id)
        return make_response(jsonify({
            "status": 202,
            "data": new_cand
        }), 202)
