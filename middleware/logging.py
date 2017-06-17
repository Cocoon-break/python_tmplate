# -*- coding: utf8 -*-

from functools import wraps
from flask import request

from utils import log


def logging_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug('[Test] request:\n' + request.headers.get('token'))
        resp = func(*args, **kwargs)
        log.debug('[Test] response:\n' + resp)
        return resp

    return wrapper
