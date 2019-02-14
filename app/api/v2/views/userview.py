import datetime
from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.usermodel import UserModel
from flask_jwt_extended import (create_access_token,
                                jwt_required, get_jwt_identity)


signup = Blueprint('signup', __name__, url_prefix='/api/v2/auth/')
login = Blueprint('login', __name__, url_prefix='/api/v2/auth/')


class UserRegister():

    @signup.route('/signup', methods=['POST'])
    def signup():
        '''Function of creating a party'''
        data = request.get_json()

        firstname = data['firstname']
        lastname = data['lastname']
        othername = data['othername']
        email = data['email']
        password = data['password']

        email_exists = UserModel.get('users', email=email)

        if email_exists:
            return make_response(jsonify({'message':
                                          'That email is taken.'}), 203)

        user = UserModel()
        user.register_user(firstname, lastname, othername,
                           email, password)

        return make_response(jsonify({
            "status": 201,
            "message": "You are registered successfully"
        }), 201)


class LoginUser():

    @login.route('/login', methods=['POST'])
    def login():

        data = request.get_json()
        try:

            email = data['email']
            password = data['password']

            if data['email'].strip() == "":
                return make_response(jsonify({"status": 400,
                                              "error": "Provide your email"}
                                             ), 400)
            if data['password'].strip() == "":
                return make_response(jsonify({"status": 400,
                                              "error":
                                              "Please enter your password"}), 400)

        except:

            return make_response(jsonify({
                "status": 400,
                "error": "You have not provided all the fields"
            }), 400)

        signeduser = UserModel()
        signeduser.get_user_by_email(email)

        expires = datetime.timedelta(minutes=3000000)
        token = create_access_token(identity=signeduser.serialize(),
                                    expires_delta=expires)

        return make_response(jsonify({
            'token': token,
            'status': 200,
            'message': 'successfully logged in'
        }), 200)
