import datetime
from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.usermodel import UserModel
from flask_jwt_extended import (create_access_token,
                                jwt_required, get_jwt_identity)
from app.api.utils import validate_login, validate_signup

signup = Blueprint('signup', __name__, url_prefix='/api/v2/auth/')
login = Blueprint('login', __name__, url_prefix='/api/v2/auth/')


class UserRegister():

    @signup.route('/signup', methods=['POST'])
    def signup():
        '''Function of creating a party'''
        errors = validate_signup(request)
        if not errors:

            data = request.get_json()

            firstname = data['firstname']
            lastname = data['lastname']
            othername = data['othername']
            email = data['email']
            password = data['password']

            if UserModel().get_user_by_email(email):
                return make_response(jsonify({"error": "Email is in Already in Use",
                                              "status": 400}), 400)

            user = UserModel()
            user.register_user(firstname, lastname, othername,
                               email, password)

            expires = datetime.timedelta(minutes=120)
            token = create_access_token(identity=user.serialize(),
                                        expires_delta=expires)

            return make_response(jsonify({
                "status": 201,
                "data": [{
                    "token": token,
                    "user": {
                        "email": email,
                        "firstname": firstname
                    },

                }]}), 201)

        else:
            return make_response(jsonify({"errors": errors,
                                          "status": 400

                                          }), 400)


class LoginUser():

    @login.route('/login', methods=['POST'])
    def login():
        errors = validate_login(request)
        if not errors:

            data = request.get_json()

            email = data['email']
            password = data['password']

            signeduser = UserModel()
            signeduser.get_user_by_email(email)

            expires = datetime.timedelta(minutes=120)
            token = create_access_token(identity=signeduser.serialize(),
                                        expires_delta=expires)

            return make_response(jsonify({
                "status": 200,
                "message": "You are successfully logged in",
                "data": [{
                    "token": token,
                    "user": {
                        "email": email
                    },

                }]}), 200)
        else:
            return make_response(jsonify({"errors": errors,
                                          "status": 400

                                          }), 400)
