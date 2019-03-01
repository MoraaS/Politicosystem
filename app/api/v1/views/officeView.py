'''Importing the classes and methods to be used in officemodel
and also all office routes'''
import re
from flask import Blueprint, make_response, request, jsonify
from app.api.v1.models.officemodel import OfficeModel, OFFICES

office_endpoints = Blueprint('office', __name__, url_prefix='/api/v1')


@office_endpoints.route('/offices', methods=['POST'])
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

        if any(office['name'] == name for office in OFFICES):
            return make_response(jsonify({
                "status": 400,
                "error": "This office already exists"
            }), 400)

    except:

        return make_response(jsonify({
            "status": 400,
            "error": "Not all fields are provided"
        }), 400)

    office = OfficeModel(name=name, office_type=office_type)
    office.create()

    return make_response(jsonify({
        "status": 201,
        "data": [{"office_id": len(OFFICES), "name": name}]
    }), 201)


@office_endpoints.route('/offices', methods=['GET'])
def get_offices():
    '''Function to get all offices'''
    return make_response(jsonify({"status": 200,
                                  "data": OfficeModel.get_all()
                                  }), 200)


@office_endpoints.route('/offices/<int:office_id>', methods=['GET'])
def get_by_id(office_id):
    '''Function to get office by id and passing the parameter id'''
    specific_office = OfficeModel.get_by_id(office_id)

    if specific_office:

        return make_response(jsonify({"status": 200,
                                      "data": specific_office}), 200)

    return make_response(jsonify({
        "status": 404,
        "error": "The office does not exist"
    }), 404)
