import re
from flask import Blueprint, make_response, request, jsonify
import json
from app.api.v2.models.officemodel import OfficeModel
from app.api.v2.models.votermodel import VoteModel
from flask_jwt_extended import (create_access_token,
                                jwt_required, get_jwt_identity)

vote_v2 = Blueprint('vote', __name__, url_prefix='/api/v2/')


@vote_v2.route('/vote', methods=['POST'])
def new_vote():
    data = request.get_json()

    try:

        office = data["office"]
        candidate = data["candidate"]

    except:

        return make_response(jsonify({
            "status": 400,
            "error": "Not all fields are provided"
        }), 400)

        newvote = VoteModel()
        newvote.create_new_vote(office, candidate, voter)

    return make_response(jsonify({'status': 201,
                                  'message': 'Vote Casted Successfully'}), 201)
