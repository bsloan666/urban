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

def find_image(phrase, animated=False, unsafe=False):
    attempts = 0

    qs = {
        "v": 1.0,
        "q": phrase,
        "imgsz": "large",
        "userip": request.remote_addr,
    }
    if not unsafe:
        qs["safe"] =  "active",

    ext_filters = ['.jpg', '.png', '.gif']
    #ext_filters = ['.jpg']
    #Kind of working :-/
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

def space_to_plus(mystr):
    return re.sub(" ","+", mystr)    


@app.route('/')
def index():

    unsafe = False
    animated = False 
    base = "http://%s"%request.environ['HTTP_HOST']
    curr = base + "/?" 
    if request.args.get('a') is not None:
        animated = True
        curr +="a=1&"
    if request.args.get('u') is not None:
        unsafe = True
        curr +="u=1"

    if request.args.get('adj') and request.args.get('noun') and request.args.get('imgurl'):
        adj = request.args.get('adj')
        noun = request.args.get('noun')
        imgurl = request.args.get('imgurl')
    else:
        adj,alt_adj,noun,alt_noun = generate.random_phrase()
        imgroot = '%s %s'%(alt_adj,alt_noun)
        imgurl = find_image(imgroot, animated, unsafe) 

    root = '%s %s'%(adj,noun)
    thisview = "http://%s?adj=%s&noun=%s&imgurl=%s"%(request.environ['HTTP_HOST'], 
        space_to_plus(adj),space_to_plus(noun), imgurl)

    

    return render_template('index.html.tpl', text=root, img=imgurl, 
        permalink=thisview, current_url=curr, baseurl=base)


if __name__ == '__main__':
    app.run(debug=True)
