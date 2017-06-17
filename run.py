# -*- coding: utf8 -*-

from app import app
from utils import config

if __name__ == '__main__':
    ip = config.appcfg.get('doudouSpace', 'ip')
    port = config.appcfg.get('doudouSpace', 'port')

    app.run(host=ip, port=port)
