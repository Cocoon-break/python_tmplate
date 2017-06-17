# -*- coding: utf8 -*-

from app import app
from flask import request, jsonify
from utils import helpers
from middleware.logging import logging_test
import json


def check_token(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('token', '')
        isPass = helpers.parse_login_token(token)
        if not isPass:
            return json.dumps({'err': 'token invalid'})
        return func(*args, **kwargs)

    return wrapper


@app.route("/")
@check_token
@logging_test
def hello():
    result = {'message': 'hello world!'}
    return json.dumps(result)
