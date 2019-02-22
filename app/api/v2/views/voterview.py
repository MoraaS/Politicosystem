import re
from flask import Blueprint, make_response, request, jsonify
import json
from app.api.v2.models.candidates import CandidatesModel
from app.api.v2.models.officemodel import OfficeModel
from app.api.v2.models.votermodel import VoteModel
from app.api.v2.models.usermodel import UserModel
from app.api.utils import login_required, validate_votes

vote_v2 = Blueprint('vote', __name__, url_prefix='/api/v2/')


@vote_v2.route('/vote', methods=['POST'])
@login_required
def new_vote():
    '''Function for creatig a new vote'''
    errors = validate_votes(request)
    if not errors:

        data = request.get_json()

        createdby = data["createdby"]
        office_id = data["office_id"]
        candidate_id = data["candidate_id"]

        if not UserModel().get_user_by_id(createdby):
            return make_response(jsonify({
                "status": 404,
                "error": "The vote id doesn't exist, enter a valid one"
            }), 400)
        # check if office exists
        if not OfficeModel().get_by_id(office_id):
            return make_response(jsonify({
                "status": 404,
                "error": "Office doesn't exist, enter a valid one"
            }), 400)

        # check if candidate exists
        if not CandidatesModel().get_by_id(candidate_id):
            return make_response(jsonify({
                "status": 404,
                "error": "Candidate doesn't exist, try a valid id"
            }), 400)

        newvote = VoteModel()
        print(newvote)

        if newvote.check_if_voter_voted(createdby, office_id):
            return make_response(jsonify({
                "status": 409,
                "error": "You have already voted for this office"
            }), 409)

        data = newvote.create_new_vote(createdby, office_id, candidate_id)

        vote_object = []
        vote = {
            "office_id": office_id,
            "office_id": office_id,
            "candidate_id": candidate_id
        }
        vote_object.append(vote)

        return make_response(jsonify({'status': 201,
                                      'message': 'Vote has been Casted Successfully'}, vote_object), 201)

    else:
        return make_response(jsonify({"errors": errors,
                                      "status": 400

                                      }), 400)


