from flask import request, make_response, jsonify
from api.v1.models.models_office import OfficeModel, offices
from flask import Flask


@app.route("/api/v1/offices", methods=['POST'])
def create_office():

    data = request.get_json()
    id = data["id"]
    name = data["name"]
    type = data["name"]

    office = OfficeModel(id, type, name)
    office.save_office()
    data = {
        "id": id,
        "name": name,
        "type": type,
    }
    return make_response(jsonify(
        {'message': 'party created successfully', 'data': data})201)
