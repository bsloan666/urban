#!/usr/bin/env python
"""
Views
"""
import os
import re
import sys
import json
import urllib
import cgi
import hashlib
from base64 import b64encode, b64decode

from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import escape
from flask import redirect

from flask_caching import Cache

import requests

import generate
import hall_of_fame

ABORT = False

# urbanator_key
GOOGLE_API_KEY = os.getenv('GOOGLE_CUSTOM_SEARCH_KEY')
GOOGLE_API_NAME = '008339482522121375689:itwzfsa-pus'

APP = Flask(__name__)
CACHE = Cache(APP, config={'CACHE_TYPE': 'simple'})

FAKE_SALT = os.getenv('FAKE_SALT', 'r01YxUMwfHJvWQak')

def find_image(phrase, animated=False, unsafe=False):
    """
    google image search API wrapper
    """
    query_search = {
        "cx": GOOGLE_API_NAME,
        "key": GOOGLE_API_KEY,
        "q": phrase,
        "searchType": "image",
        "imgSize": "large",
        "imgType": "photo",
        "prettyPrint": "true",
        "userIp": request.remote_addr,
    }
    if not unsafe:
        query_search["safe"] = "medium"
    else:
        query_search["safe"] = "off"

    ext_filters = ['.jpg', '.png', '.gif']
    #ext_filters = ['.jpg']
    #Kind of working :-/
    if animated:
        query_search["fileType"] = "gif"
        ext_filters = ['.gif']

    resp = requests.get("https://www.googleapis.com/customsearch/v1", params=query_search)
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
    """
    convert spaces to pluses for some reason
    """
    return re.sub(" ", "+", mystr)

def colon_to_pct(mystr):
    """
    ...some sort of HTL escaping, maybe?
    """
    return re.sub(":", "%3A", mystr)


def protect_context(context):
    """
    how to obscure google image search API key
    """
    hashed = hashlib.sha1(
        '{adj}:{salt}:{img}:{noun}'.format(
            adj=context['adj'],
            salt=FAKE_SALT,
            img=context['img'],
            noun=context['noun'],
        ).encode('utf-8')
    )
    return hashed.hexdigest()

def verify_context(context):
    """
    more of the same
    """
    context_hash = context.pop('hash')
    check_hash = protect_context(context)
    return context_hash == check_hash

@APP.route('/')
def index():
    """
    main entrypoint
    """
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
        adj, alt_adj, noun, alt_noun = generate.random_phrase_2()
        imgroot = '%s %s'%(adj, noun)
        if random:
            imgroot = '%s %s'%(alt_adj, alt_noun)
        imgurl = find_image(imgroot, animated, unsafe)
        print("IMAGE URL",imgurl)
        imgenc = b64encode(bytes(imgurl, 'utf-8'))

    current_context = {'adj':adj, 'noun':noun, 'img':imgurl}
    hashed_context = protect_context(current_context)
    url_context = {'hash':hashed_context}
    url_context.update(current_context)

    root = '%s %s'%(adj, noun)
    info_data = b64encode(bytes(json.dumps(url_context), 'utf-8'))
    thisview = "{0}://{1}/{2}".format(
        request.environ['wsgi.url_scheme'],
        request.environ['HTTP_HOST'],
        info_data
    )

    if redirect_to_url:
        return redirect('/{0}'.format(info_data))

    quote = urllib.parse.quote(colon_to_pct(thisview))

    return render_template('index.html.tpl', text=root, img=imgurl,
                           permalink=thisview, current_url=curr, baseurl=base, quotelink=quote,
                           animchecked=animchecked, unsfchecked=unsfchecked,
                           randchecked=randchecked)


@APP.route('/<hash_value>')
def saved(hash_value):
    """
    hmf
    """
    try:
        json_data = b64decode(hash_value)
        data = json.loads(json_data)
        if not verify_context(data):
            return redirect('/')
    except:
        return redirect('/')

    return render_template(
        'detail.html.tpl',
        text='{0} {1}'.format(data['adj'], data['noun']),
        img=data['img'],
        imgenc=request.url,
        permalink=request.url,
        quotelink=urllib.parse.quote(colon_to_pct(request.url)),
    )


@APP.route('/hall-of-fame')
def hall_of_fame_func():
    """
    hall-of-fame entry point
    """
    base = "http://%s" % request.environ['HTTP_HOST']
    curr = base
    favorites_cache = CACHE.get('favorites')
    if not favorites_cache:
        data = hall_of_fame.load_faves()
        favorites = hall_of_fame.process_faves(data)
        CACHE.set('favorites', json.dumps(favorites))
    else:
        favorites = json.loads(favorites_cache)

    return render_template('halloffame.html.tpl', favorites=favorites)

if __name__ == '__main__':
    APP.run(debug=True)
