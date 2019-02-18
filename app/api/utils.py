import re
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
import json


def validate_signup(request):
    data = request.get_json()
    errors = []
    signup_keys = ['firstname', 'lastname', 'othername',
                   'email', 'password']
    for key in signup_keys:

        if key not in request.json:
            error = {key: "Field must be provided"}
            errors.append(error)

    if errors:
        return errors
    if data['firstname'].strip() == "":

        error = {"firstname": "Firstname is required"}
        errors.append(error)
    if data['lastname'].strip() == "":
        error = {"firstname": "Lastname is required"}
        errors.append(error)
    if data['othername'].strip() == "":
        error = {"firstname": "Othername is required"}
        errors.append(error)
    if data['email'].strip() == "":
        error = {"email": "email is required"}
        errors.append(error)
    if data['password'].strip() == "":
        error = {"password": "password is required"}
        errors.append(error)


def validate_login(request):
    data = request.get_json()

    errors = []
    login_keys = ['email', 'password']
    for key in login_keys:

        if key not in request.json:

            error = {key: "Field must be provided"}

            errors.append(error)

    if errors:
        return errors

    if data['email'].strip() == "":
        error = {"email": "Provide your email"}
        errors.append(error)

    if data['password'].strip() == "":
        error = {"password": "Please enter your password"}
        errors.append(error)

    return errors


def validate_office(request):
    data = request.get_json()
    errors = []
    office_keys = ["name", "office_type"]

    for key in office_keys:

        if key not in request.json:

            error = {key: "Field must be provided"}

            errors.append(error)

    if errors:
        return errors

    if data['name'].strip() == "":
        error = {"name": "Provide your office name"}
        errors.append(error)

    if data['office_type'].strip() == "":
        error = {"office_type": "Provide the office type"}
        errors.append(error)

    return errors
