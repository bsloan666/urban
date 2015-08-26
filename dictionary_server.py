#!/usr/bin/env python

import os
import re 
from functools import wraps
import sys
import json
import threading
import time
import yaml
import cgi

from dd.runtime import api
api.load('flask')
from flask import Flask
from flask import make_response
from flask import request 
import generate

abort = False

app = Flask(__name__)

@app.route('/urbandictionaryphrases')
def toplevel():
    root = generate.random_phrase()
    head="""
        <html>
        <head>
        <style>
        h2 {text-align:center;}
        p {text-align:center;}
        </style>
        </head>
        <body><br><br><br><br><br><h2><font face=arial>"""
    foot="""
        </font></h2></body>
        </html>"""
    resp = make_response("%s%s%s"%(head,cgi.escape(root),foot))
    resp.headers['Content-Type'] = 'text/html'
    resp.headers['access-control-allow-origin'] = '*'
    return resp 

if __name__ == '__main__':
    app.run()

