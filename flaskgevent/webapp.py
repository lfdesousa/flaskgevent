#!/usr/bin/env python

"""
Example flask webapp using asynchronous network requests through gevent
usage: python webapp.py
"""

import json
from flask import Flask, request, make_response, abort, Blueprint, jsonify
import sys
import urllib2
import logging
from logging.handlers import TimedRotatingFileHandler
from urllib2 import URLError
# import memcache
import gevent
from gevent import monkey
monkey.patch_all()

app = Flask(__name__, instance_relative_config = True)

app.config.from_object('flaskgevent.my_config')
app.config.from_envvar('MY_CONFIG',
                       silent = True)

def _setup_logger(stdout = False):
    """Setup loggers
    :type: bool
    :param stdout: Whether or not to log to stdout"""
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(module)s.%(funcName)s() - %(message)s')
    try:
        handlers = [TimedRotatingFileHandler(app.config['LOG_FILE']),]
    except IOError:
        handlers = [logging.StreamHandler(),]
    if stdout:
        handlers = [logging.StreamHandler(),]
    loggers = [app.logger, logging.getLogger('zad.main'),]
    for handler in handlers:
        handler.setFormatter(formatter)
        if app.config['DEBUG']:
            handler.setLevel(logging.DEBUG)
        else:
            handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)
        for logger in loggers:
            logger.addHandler(handler)
    app.logger.debug("Debug is %s" % (app.config['DEBUG'],))

@app.route('/')
def index():
    """Get static json data"""
    data = { "somekey" : "somedata" }
    resp = make_response(json.dumps(data), 200)
    resp.headers["Content-Type"] = "application/json"
    return resp

if __name__ == '__main__':
    _setup_logger(stdout = True)
    app.run(debug = True)
