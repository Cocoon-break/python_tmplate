# -*- coding: utf8 -*-
"""Logging for frontline

"""


import logging
from logging.handlers import RotatingFileHandler
from . import config

log_filename = config.appcfg.get('doudouSpace', 'log_file')
logging.basicConfig(level=logging.DEBUG,
                    format='%(filename)s:%(lineno)s - %(asctime)s %(levelname)s %(message)s',
                    filename=log_filename,
                    filemode='a')

logger = logging.getLogger()
log_handler = logging.handlers.WatchedFileHandler(log_filename)
logger.addHandler(log_handler)


def debug(msg):
    # logging.debug(msg)
    logger.debug(msg)


def info(msg):
    # logging.info(msg)
    logger.info(msg)


def warning(msg):
    # logging.warning(msg)
    logger.warning(msg)


def error(msg):
    # logging.error(msg)
    logger.error(msg)
