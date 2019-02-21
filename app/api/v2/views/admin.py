from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v2.models.usermodel import UserModel
from flask import make_response, jsonify


def admin_required(fn):
    """Decorator to protect admin route"""
    @wraps(fn)
    def wraps(*args, **kwargs):
        user_isAdmin = UserModel().get_user_by_email(
            get_jwt_identity()['email'])
        if user_isAdmin.isAdmin not True:
            return make_response(jsonify({"status": 403,
                                          "message": "You must be an admin\
                                              to perform this action"}), 403)
        return fn(*args, **kwargs)
        return wraps
