import re
from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.officemodel import OfficeModel
import json

office_v2 = Blueprint('office2', __name__, url_prefix='/api/v2/')


@office_v2.route('/offices', methods=['POST'])
def create_office():
    '''Function to create a new office'''
    data = request.get_json()
    try:
        name = data['name']
        office_type = data['office_type']

        if data['name'].strip() == "":
            return make_response(jsonify({"status": 400,
                                          "error": "Office name cant be blank"}
                                         ), 400)
        if data['office_type'].strip() == "":
            return make_response(jsonify({"status": 400,
                                          "error":
                                          "office_type cant be blank"}), 400)
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

    except:

        return make_response(jsonify({
            "status": 400,
            "error": "Not all fields are provided"
        }), 400)

    office = OfficeModel()
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
