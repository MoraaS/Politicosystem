import re
from flask import jsonify, request, make_response
# from flask_jwt_extended import get_jwt_identity
from functools import wraps
import json
import jwt
import os


def validate_signup(request):
    data = request.get_json()
    errors = []
    signup_keys = ['firstname', 'lastname', 'othername',
                   'email', 'phonenumber', 'password', 'passporturl']
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

    if data['phonenumber'].strip() == "":
        error = {"phonenumber": "phonenumber is required"}
        errors.append(error)

    if data['password'].strip() == "":
        error = {"password": "password is required"}
        errors.append(error)

    if data['passporturl'].strip() == "":
        error = {"passporturl": "passporturl is required"}
        errors.append(error)

    return errors


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


def validate_parties(request):
    data = request.get_json()

    errors = []
    party_keys = ["name", "hqaddress", "logourl"]

    for key in party_keys:

        if key not in request.json:

            error = {key: "Field must be provided"}

            errors.append(error)

    if errors:
        return errors

    if data['name'].strip() == "":
        error = {"name": "Provide your party name"}
        errors.append(error)

    if data['hqaddress'].strip() == "":
        error = {"hqaddress": "Provide the hqaddress"}
        errors.append(error)

    if data['logourl'].strip() == "":
        error = {"logourl": "Provide the logourl"}
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


def validate_votes(request):
    data = request.get_json()

    errors = []
    voters_keys = ["createdby", "office_id", "candidate_id"]

    for key in voters_keys:

        if key not in request.json:

            error = {key: "Field must be provided"}

            errors.append(error)

    if errors:
        return errors

    if data['createdby'].strip() == "":
        error = {"createdby": "Provide your voters id"}
        errors.append(error)

    if data['office_id'].strip() == "":
        error = {"office_id": "Enter the office id you want to vote for"}
        errors.append(error)

    if data['candidate_id'].strip() == "":
        error = {"candidate_id": "Provide the the id youre voting for"}
        errors.append(error)

    return errors


"""Decorators"""


def login_required(fn):
    """Decorator to protect admin route"""
    @wraps(fn)
    def token_decorator(*args, **kwargs):

        if "Authorization" in request.headers:
            token = request.headers['Authorization']
        else:
            return make_response(jsonify({"error": "This method requires you to enter a token"}), 403)

        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'))
        except Exception as e:
            return make_response(jsonify({"message": "Token is required to access the method"}))

        return fn(*args, **kwargs)
    return token_decorator


def admin_required(fn):
    """Decorator to protect admin routes"""
    @wraps(fn)
    def admin_decorator(*args, **kwargs):

        if "Authorization" in request.headers:
            token = request.headers['Authorization']
        else:
            return make_response(jsonify({"error": "Admin Token is required in order to access the method"}), 403)

        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'))
            if data['isAdmin'] != True:

                return make_response(jsonify({"message": "To access the method admin token is required"}), 403)
        except Exception as e:
            return make_response(jsonify({"message": "token is invalid, put in the assigned token"}), 403)

        return fn(*args, **kwargs)
    return admin_decorator
