#!/usr/bin/env python
import sys
import os
from random import shuffle

def init_db(fname):
    handle = open(fname, 'r')
    lines = handle.readlines()
    handle.close()
    return lines


def random_phrase():
    adjs = init_db('adjectives.db')
    nouns = init_db('nouns.db')

    shuffle(adjs)
    shuffle(nouns)

    a_range = range(len(adjs))
    n_range = range(len(nouns))

    shuffle(a_range)
    shuffle(n_range)

    return "%s %s"%(adjs[a_range[0]].strip(), nouns[n_range[0]].strip())

if __name__ in "__main__":
    print random_phrase()

