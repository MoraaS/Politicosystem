from flask import Flask, Blueprint, make_response, request, jsonify
from app.api.v1.models.officeModel import OfficeModel, offices


office_endpoints = Blueprint('office', __name__, url_prefix='/api/v1')


@office_endpoints.route('/offices', methods=['POST'])
def create_office():
    data = request.get_json()
    try:
        name = data['name']
        office_type = data['office_type']

    except:

        return make_response(jsonify({
            "status": 400,
            "error": "You have not provided all the fields"
        }), 400)

    office = OfficeModel(name=name, office_type=office_type)
    office.create()

    return make_response(jsonify({
        "status": 201,
        "data": [{"office_id": len(offices)-1, "name": name}]
    }), 201)


@office_endpoints.route('/offices', methods=['GET'])
def get_offices():
    return make_response(jsonify({"status": 200,
                                  "data": OfficeModel.get_all()
                                  }), 200)


@office_endpoints.route('/offices/<int:office_id>', methods=['GET'])
def get_by_id(office_id):

    specific_office = OfficeModel.get_by_id(office_id)

    if specific_office:

        return make_response(jsonify({"status": 200,
                                      "data": specific_office}), 200)

    return make_response(jsonify({
        "status": 404,
        "error": "The office does not exist"
    }), 404)
