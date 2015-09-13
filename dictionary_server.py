#!/usr/bin/env python

import os
import re
import sys
import json
import urllib2
import cgi
from base64 import b64encode,b64decode

from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import escape

from flask.ext.cache import Cache

import requests

import generate
import hall_of_fame

abort = False

app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

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

def colon_to_pct(mystr):
    return re.sub(":","%3A", mystr)

@app.route('/')
def index():

    random = False
    unsafe = False
    animated = False
    base = "http://%s/"%request.environ['HTTP_HOST']
    curr = base
    animchecked = ""
    unsfchecked = ""
    randchecked = ""
    if request.args.get('a') is not None:
        animated = True
        animchecked = "checked"
    if request.args.get('u') is not None:
        unsafe = True
        unsfchecked = "checked"
    if request.args.get('r') is not None:
        random = True
        randchecked = "checked"

    if request.args.get('adj') and request.args.get('noun'):
        adj = escape(request.args.get('adj'))
        noun = escape(request.args.get('noun'))
        if request.args.get('imgurl'):
            imgurl = escape(request.args.get('imgurl'))
            imgenc = b64encode(imgurl) 
        elif request.args.get('imgenc'):
            imgenc = request.args.get('imgenc')
            imgurl = escape(b64decode(imgenc))
    else:
        adj,alt_adj,noun,alt_noun = generate.random_phrase_2()
        imgroot = '%s %s'%(adj,noun)
        if random:
            imgroot = '%s %s'%(alt_adj,alt_noun)
        imgurl = find_image(imgroot, animated, unsafe)
        imgenc = b64encode(imgurl)

    root = '%s %s'%(adj,noun)
    thisview = "http://%s/?adj=%s&noun=%s&imgenc=%s"%(request.environ['HTTP_HOST'],
        space_to_plus(adj),space_to_plus(noun), imgenc)

    quote=urllib2.quote(colon_to_pct(thisview))

    return render_template('index.html.tpl', text=root, img=imgurl,
        permalink=thisview, current_url=curr, baseurl=base, quotelink=quote,
        animchecked=animchecked, unsfchecked=unsfchecked, randchecked=randchecked)


@app.route('/hall-of-fame')
def hallOfFame():
    base = "http://%s" % request.environ['HTTP_HOST']
    curr = base
    favorites_cache = cache.get('favorites')
    if not favorites_cache:
        data = hall_of_fame.load_faves()
        favorites = hall_of_fame.process_faves(data)
        cache.set('favorites', json.dumps(favorites))
    else:
        favorites = json.loads(favorites_cache)

    return render_template('halloffame.html.tpl', favorites=favorites)

if __name__ == '__main__':
    app.run(debug=True)
