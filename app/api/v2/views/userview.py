from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.usermodel import UserModel


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
        email = data['email']
        password = data['password']

        signeduser = UserModel()
        signeduser.get_user_by_email(email)

        return make_response(jsonify({
            'status': 200,
            'message': 'successfully logged in'
        }), 200)
