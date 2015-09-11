import os
import sys
import re

def parse_url(url):
    data = {}
    (home, args) = re.split("\?",url)
    keyvalarray = re.split("&", args)

    for keyval in keyvalarray:
        (key,val) = re.split("=", keyval)
        data[key] = val
    
    return data

def table(contents):
   return '<table align="center" border="0" cellpadding="10">\n'+contents+'\n</table>\n'

def row(contents):
    return '<tr>'+contents+'</tr>\n'

def column(contents):
    return '<td align=center>'+contents+'</td>'

def img(adj,noun,link):
    return '<img align=center height="128" src="'+link+'" alt="'+adj+' '+noun+'"/>' 

def link(adj,noun,img, link):
    adj = re.sub('\+',' ',adj)
    noun = re.sub('\+',' ',noun)
    return '<a href="'+link+'"><b>'+adj+' '+noun+'</b><br/><br/>'+img+'</a>'

def load_faves():
    handle = open('favorites.txt','r')
    lines = handle.readlines()
    handle.close()
    return lines

def build_table():
    faves = load_faves()
    myrow = "" 
    contents = ""
    columns = 0
    for fave in faves[::-1]:
        data = parse_url(fave)
        myrow += column(link(data['adj'], data['noun'], 
            img(data['adj'], data['noun'],data['imgurl']), fave))
        columns = columns+1
        if columns >= 3:
            columns = 0
            contents += row(myrow)
            myrow = ""

    return table(contents)

