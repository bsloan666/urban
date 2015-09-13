import os
import sys
import re
import urlparse

from random import Random

def parse_url(url):
    data = {}
    (home, args) = re.split("\?",url)
    keyvalarray = re.split("&", args)

    for keyval in keyvalarray:
        (key,val) = re.split("=", keyval)
        data[key] = val

    return data

def random_color():
    r = Random()
    red = hex(r.randint(220,255))
    green = hex(r.randint(220,255))
    blue = hex(r.randint(220,255))
    return "#"+red[-2:]+green[-2:]+blue[-2:]


def table(contents):
   return '<table align="center" border="0" cellpadding="10">\n'+contents+'\n</table>\n'

def row(contents):
    return '<tr>'+contents+'</tr>\n'

def column(contents, color):
    return '<td align=center bgcolor="'+color+'">'+contents+'</td>'

def img(adj,noun,link):
    return '<img align=center height="128" src="'+link+'" alt="'+adj+' '+noun+'"/>'

def link(adj,noun,img, link):
    adj = re.sub('\+',' ',adj)
    noun = re.sub('\+',' ',noun)
    return '<a href="'+link+'"><b>'+adj+' '+noun+'</b><br/><p>'+img+'</p><br/><br/></a>'

def load_faves():
    handle = open('favorites.db','r')
    lines = handle.readlines()
    handle.close()
    return lines

def process_faves(fav_lines):
    faves = []
    for fav in fav_lines:
        url_data = urlparse.urlparse(fav.strip())
        parsed_url = urlparse.parse_qs(url_data.query)
        parsed_url['url'] = fav.strip()
        faves.append(parsed_url)
    return list(reversed(faves))

def build_table():
    faves = load_faves()
    myrow = ""
    contents = ""
    columns = 0
    for fave in faves[::-1]:
        data = parse_url(fave)
        color = '#FFFFFF'
        myrow += column(link(data['adj'], data['noun'],
            img(data['adj'], data['noun'],data['imgurl']), fave), color)
        columns = columns+1
        if columns >= 3:
            columns = 0
            contents += row(myrow)
            myrow = ""

    return table(contents)
