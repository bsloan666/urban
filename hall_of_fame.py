"""
    Generate the hall-of-fame page
"""

import re
from urllib.parse import urlparse, parse_qs
import json
from base64 import b64decode
from random import Random

def parse_url(url):
    """
    Given a URL, create a dictionary of key/value pairs
    """
    data = {}
    (_, args) = re.split(r"\?", url)
    keyvalarray = re.split(r"&", args)

    for keyval in keyvalarray:
        (key, val) = re.split(r"=", keyval)
        data[key] = val

    return data

def random_color():
    """
    return a random color
    """
    rand = Random()
    red = hex(rand.randint(220, 255))
    green = hex(rand.randint(220, 255))
    blue = hex(rand.randint(220, 255))
    return "#"+red[-2:]+green[-2:]+blue[-2:]


def table(contents):
    """
    wrap contents in an HTML table
    """
    return '<table align="center" border="0" cellpadding="10">\n'+contents+'\n</table>\n'

def row(contents):
    """
    wrap contents in an HTML row
    """
    return '<tr>'+contents+'</tr>\n'

def column(contents, color):
    """
    wrap contents in an HTML table cell
    """
    return '<td align=center bgcolor="'+color+'">'+contents+'</td>'

def img(adj, noun, _link):
    """
    create an image tag
    """
    return '<img align=center height="128" src="'+_link+'" alt="'+adj+' '+noun+'"/>'

def link(adj, noun, _img, _link):
    """
    create an HTML link
    """
    adj = re.sub(r'\+', ' ', adj)
    noun = re.sub(r'\+', ' ', noun)
    return '<a href="'+_link+'"><b>'+adj+' '+noun+'</b><br/><p>'+_img+'</p><br/><br/></a>'

def load_faves():
    """
    load the table of favorites links
    """
    handle = open('favorites.db', 'r')
    lines = handle.readlines()
    handle.close()
    return lines

def process_faves(fav_lines):
    """
    build a list of dictionaries representing the favorites
    """
    faves = []
    for fav in fav_lines:
        url_data = urlparse(fav.strip())
        if '?' in fav:
            parsed_url = parse_qs(url_data.query)
            parsed_url['url'] = fav.strip()
        else:
            encoded = re.split('/', fav)[-1].strip()
            json_data = b64decode(encoded)
            parsed_url = json.loads(json_data)
            parsed_url['imgurl'] = [str(parsed_url['img'])]
            parsed_url['noun'] = [str(parsed_url['noun'])]
            parsed_url['adj'] = [str(parsed_url['adj'])]
            parsed_url['url'] = fav.strip()
            parsed_url.pop('img', 0)
        faves.append(parsed_url)
    return list(reversed(faves))

def build_table():
    """
    generate a grid of images and phrases
    """
    faves = load_faves()
    myrow = ""
    contents = ""
    columns = 0
    for fave in faves[::-1]:
        data = parse_url(fave)
        color = '#FFFFFF'
        myrow += column(link(data['adj'], data['noun'],
                             img(data['adj'], data['noun'],
                                 data['imgurl']), fave), color)
        columns = columns+1
        if columns >= 3:
            columns = 0
            contents += row(myrow)
            myrow = ""

    return table(contents)
