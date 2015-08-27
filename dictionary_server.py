#!/usr/bin/env python

import os
import re 
import sys
import json 
import urllib2
import cgi

from flask import Flask
from flask import make_response
from flask import request 
import generate

abort = False

app = Flask(__name__)

def find_image(phrase):
    attempts = 0
    phrase = re.sub(' ','+',phrase)
    while attempts < 3:
        try:
            webstr = \
                "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&safe=active&imgsz=large"%(
                    cgi.escape(phrase))
            print cgi.escape(phrase)    
            print webstr
            response = urllib2.urlopen(webstr,timeout = 5)
                    
            content = response.read()
            results = json.loads(content)
            for imgdict in results['responseData']['results']:
                if imgdict['url'].endswith('jpg'):
                    return imgdict['url']
                
        except urllib2.URLError as e:
            attempts += 1
            print type(e)

@app.route('/urban')
def toplevel():
    root = generate.random_phrase()
    head="""
        <html>
        <head>
        <style>
        h2 {text-align:center;}
        p {text-align:center;}
        img.displayed {
            display: block;
            margin-left: auto;
            margin-right: auto }
        </style>
        </head>
        <body><br><br><br><br><br><h2><font face=arial>"""
    foot="""
        </font></h2><br><img class="displayed" src="%s" alt="%s" align="middle"/></body>
        </html>"""
    resp = make_response("%s%s%s"%(head,cgi.escape(root),foot%(find_image(root),root)))
    resp.headers['Content-Type'] = 'text/html'
    resp.headers['access-control-allow-origin'] = '*'
    return resp 

if __name__ == '__main__':
    app.run()

