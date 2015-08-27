#!/usr/bin/env python

import os
import re
import sys
import json
import urllib2
import cgi

from flask import Flask
from flask import make_response
from flask import render_template
from flask import request

import requests

import generate

abort = False

app = Flask(__name__)


def find_image(phrase, animated=False):
    attempts = 0

    qs = {
        "v": 1.0,
        "q": phrase,
        "safe": "active",
        "imgsz": "large",
        "userip": request.remote_addr,
    }

    ext_filters = ['.jpg', '.png', '.gif']
    # Kind of working :-/
    if animated:
        qs["as_filetype"] = "gif"
        ext_filters = ['.gif']

    resp = requests.get("https://ajax.googleapis.com/ajax/services/search/images", params=qs)
    if resp.status_code == 200:
        results = resp.json()
        for imgdict in results['responseData']['results']:
            img_url = imgdict['url']
            _, ext = os.path.splitext(img_url)
            if ext.lower() in ext_filters:
                return img_url

    return ""


@app.route('/')
def index():
    seed = generate.random_seed()
    if request.args.get('s'):
        seed = request.args.get('s').strip()

    animated = False
    if request.args.get('a') is not None:
        animated = True

    root = generate.random_seeded_phrase(seed)
    return render_template('index.html.tpl', text=root, img=find_image(root, animated), seed=seed)


if __name__ == '__main__':
    app.run(debug=True)
