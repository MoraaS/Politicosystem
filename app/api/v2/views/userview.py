import re
import datetime
import jwt
from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.usermodel import UserModel
# from flask_jwt_extended import (create_access_token,
#                                 jwt_required, get_jwt_identity)
from app.api.utils import validate_login, validate_signup
from werkzeug.security import check_password_hash
import os

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
            phonenumber = data['phonenumber']
            password = data['password']
            passporturl = data['passporturl']
            isAdmin = data['isAdmin']

            if data['firstname'].isalpha() is False:
                return make_response(jsonify({"status": 400, "message": "firstname should be alphabets"}), 400)

            if data['lastname'].isalpha() is False:
                return make_response(jsonify({"status": 400, "message": "lastname should be alphabets"}), 400)

            if (len(password) < 8):
                return make_response(jsonify({
                    "status": 400,
                    "error": "Password cannot be less than 8 characters"
                }), 400)

            if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$", password):
                return make_response(jsonify({
                    "status": 400,
                    "error": "Password must have atleast one uppercase,\
                        lowercase and special character"}), 400)

            if not re.match("^[a-zA-Z0-9_+-]+@[a-zA-Z-]+\.[a-zA-Z0-]+$", email):
                return make_response(jsonify({
                    "status": 400,
                    "error": "Wrong email format try abc@xyz.com"}), 400)

            user = UserModel(firstname, lastname, othername,
                             email, phonenumber, password, passporturl, isAdmin)

            if user.get_user_by_email(email):
                return make_response(jsonify({"error": "Email is in Already in Use",
                                              "status": 400}), 400)

            user.register_user()

            expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=120)
            token = jwt.encode(
                {'email': email, 'isAdmin': isAdmin,
                    'exp': expires}, os.getenv('SECRET_KEY'))

            user_object = []
            user = {
                "firstname": firstname,
                "lastname": lastname,
                "othername": othername,
                "email": email,
                "phonenumber": phonenumber,
                "password": password,
                "passporturl": passporturl,
                "isAdmin": isAdmin
            }
            user_object.append(user)

            return make_response(jsonify({
                "status": 201,
                "message": "Account Created Successfully",
                "data": [{"token": token.decode('UTF-8')}, user_object]}), 201)

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

            signeduser = UserModel(email, password)

            loged_user = signeduser.get_user_by_email(email)
            isAdmin = loged_user["isadmin"]

            if not loged_user:
                return make_response(jsonify({"status": 404,
                                              "Error": "The email you entered\
                                                  doesnt exist"}), 404)
            if not check_password_hash(loged_user["password"], password):
                return make_response(jsonify({"status": 404,
                                              "Error": "The password you\
                                                  entered doesnt exist"}), 404)

            expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=120)
            token = jwt.encode(
                {'email': email, 'isAdmin': isAdmin,
                    'exp': expires}, os.getenv('SECRET_KEY'))
            userlogin_object = []
            user = {
                "email": email,
                "password": password
            }
            userlogin_object.append(user)

            return make_response(jsonify({
                "status": 200,
                "message": "You are successfully logged in",
                "data": [{
                    "token": token.decode('UTF-8')},
                    userlogin_object]

            }), 200)
        else:
            return make_response(jsonify({"errors": errors,
                                          "status": 400

                                          }), 400)
