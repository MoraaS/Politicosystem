from flask import Flask, Blueprint, make_response, request, jsonify
from app.api.v1.models.officeModel import OfficeModel


office_endpoints = Blueprint('office', __name__, url_prefix='/api/v1')


@office_endpoints.route('/offices', methods=['POST'])
def create_office():
    data = request.get_json()
    try:

        office_id = data['office_id']
        name = data['name']
        office_type = data['office_type']

    except:

        return make_response(jsonify({
            "status": 400,
            "error": "You have not provided all the fields"
        }), 400)

    office = OfficeModel(office_id=office_id, name=name,
                         office_type=office_type)
    office.create()

    return make_response(jsonify({
        "status": 201,
        "data": [{"office_id": office_id, "name": name}]
    }), 201)


@office_endpoints.route('/offices', methods=['GET'])
def get_offices():
    return make_response(jsonify({"status": 200,
                                  "data": OfficeModel.get_all()
                                  }), 200)


@office_endpoints.route('/offices/<int:office_id>', methods=['GET'])
def get_by_id(office_id):

