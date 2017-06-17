# -*- coding: utf8 -*-
import hashlib
from utils import config

token_salt = config.appcfg.get('userConfig', 'token_salt')


def generate_login_token(userId):
    strUserId = str(userId)
    sha1 = hashlib.sha1()
    sha1.update(strUserId)
    sha1.update(token_salt)
    return strUserId + ";" + sha1.hexdigest()


def parse_login_token(token):
    try:
        [userId, sha1Str] = token.split(';', 1)
        sha1 = hashlib.sha1()
        sha1.update(userId)
        sha1.update(token_salt)
        result = sha1.hexdigest()
        if (result == sha1Str):
            return True
        else:
            return False
    except Exception:
        return False


# if __name__ == '__main__':
#     token = generate_login_token('1')
#     print 'generate_token:', token
#     parse_login_token(token)
