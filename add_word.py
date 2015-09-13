#!/usr/bin/env python

import os
import sys
import re

def load_file(fname):
    handle = open(fname, "r")
    lines = handle.readlines()
    handle.close()
    return lines

def save_file(fname, lines):
    handle = open(fname, "w")
    for line in sorted(lines):
        handle.write(line)
    handle.close()

    
if __name__ in "__main__":
    type = sys.argv[1]
    if type.startswith('a'):
        entry = " ".join(sys.argv[2:]).title()+'\n'
        adjs = load_file("adj.show.db")
        if not entry in adjs:
            adjs.append(entry)
            save_file("adj.show.db", adjs)
        else:
            print entry.strip(),"is already in adj.show.db"
        adjs = load_file("adj.hide.db")
        if not entry in adjs:
            adjs.append(entry)
            save_file("adj.hide.db", adjs)
        else:
            print entry.strip(),"is already in adj.hide.db"
    elif type.startswith('n'):
        entry = " ".join(sys.argv[2:]).title()+'\n'
        nouns = load_file("noun.show.db")
        if not entry in nouns:
            nouns.append(entry)
            save_file("noun.show.db", nouns)
        else:
            print entry.strip(),"is already in noun.show.db"
        nouns = load_file("noun.hide.db")
        if not entry in nouns:
            nouns.append(entry)
            save_file("noun.hide.db", nouns)
        else:
            print entry.strip(),"is already in noun.hide.db"
