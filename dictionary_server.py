#!/usr/bin/env python

import os
import re
import sys
import json
import urllib2
import cgi
import hashlib
from base64 import b64encode,b64decode

from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import escape
from flask import redirect

from flask.ext.cache import Cache

import requests

import generate
import hall_of_fame

abort = False

# urbanator_key
google_api_key = os.getenv('GOOGLE_CUSTOM_SEARCH_KEY') 
#google_api_name = 'urbansearch-1168'
google_api_name = '008339482522121375689:itwzfsa-pus'

app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

FAKE_SALT = os.getenv('FAKE_SALT', 'r01YxUMwfHJvWQak')

def find_image(phrase, animated=False, unsafe=False):
    attempts = 0

    qs = {
        "cx": google_api_name,
        "key": google_api_key,
        "q": phrase,
        "searchType": "image",
        "imgSize": "large",
        "imgType": "photo",
        "prettyPrint": "true",
        "userIp": request.remote_addr,
    }
    if not unsafe:
        qs["safe"] =  "medium"
    else:
        qs["safe"] =  "off"

    ext_filters = ['.jpg', '.png', '.gif']
    #ext_filters = ['.jpg']
    #Kind of working :-/
    if animated:
        qs["fileType"] = "gif"
        ext_filters = ['.gif']

    resp = requests.get("https://www.googleapis.com/customsearch/v1", params=qs)
    if resp.status_code == 200:
        results = resp.json()
        #print "Results:",str(results)
        for imgdict in results['items']:
            img_url = imgdict['link']
            _, ext = os.path.splitext(img_url)
            if ext.lower() in ext_filters:
                return img_url
    else:
        pass
        #print "Response:",resp.__dict__

    return ""

def space_to_plus(mystr):
    return re.sub(" ","+", mystr)

def colon_to_pct(mystr):
    return re.sub(":","%3A", mystr)


def protect_context(context):
    hashed = hashlib.sha1(
        '{adj}:{salt}:{img}:{noun}'.format(
            adj=context['adj'],
            salt=FAKE_SALT,
            img=context['img'],
            noun=context['noun'],
        )
    )
    return hashed.hexdigest()

def verify_context(context):
    context_hash = context.pop('hash')
    check_hash = protect_context(context)
    return (context_hash == check_hash)

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

    redirect_to_url = False
    if request.args.get('adj') and request.args.get('noun'):
        adj = escape(request.args.get('adj'))
        noun = escape(request.args.get('noun'))
        if request.args.get('imgurl'):
            imgurl = escape(request.args.get('imgurl'))
            imgenc = b64encode(imgurl)
        elif request.args.get('imgenc'):
            imgenc = request.args.get('imgenc')
            imgurl = escape(b64decode(imgenc))
        redirect_to_url = True
    else:
        adj,alt_adj,noun,alt_noun = generate.random_phrase_2()
        imgroot = '%s %s'%(adj,noun)
        if random:
            imgroot = '%s %s'%(alt_adj,alt_noun)
        imgurl = find_image(imgroot, animated, unsafe)
        imgenc = b64encode(imgurl)

    current_context = {'adj': adj, 'noun': noun, 'img': imgurl}
    hashed_context = protect_context(current_context)
    url_context = {'hash': hashed_context}
    url_context.update(current_context)

    root = '%s %s'%(adj,noun)
    info_data = b64encode(json.dumps(url_context))
    thisview = "{0}://{1}/{2}".format(
        request.environ['wsgi.url_scheme'],
        request.environ['HTTP_HOST'],
        info_data
    )

    if redirect_to_url:
        return redirect('/{0}'.format(info_data))

    quote=urllib2.quote(colon_to_pct(thisview))

    return render_template('index.html.tpl', text=root, img=imgurl,
        permalink=thisview, current_url=curr, baseurl=base, quotelink=quote,
        animchecked=animchecked, unsfchecked=unsfchecked, randchecked=randchecked)


@app.route('/<hash_value>')
def saved(hash_value):
    json_data = b64decode(hash_value)
    data = json.loads(json_data)
    if not verify_context(data):
        return redirect('/')

    return render_template(
        'detail.html.tpl',
        text='{0} {1}'.format(data['adj'], data['noun']),
        img=data['img'],
        imgenc=request.url,
        permalink=request.url,
        quotelink=urllib2.quote(colon_to_pct(request.url)),
    )


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
