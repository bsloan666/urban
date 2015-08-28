#!/usr/bin/env python
import sys
import os
import time
import string
from random import shuffle, Random

VALUES = string.ascii_letters + string.digits

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


def random_seed():
    rand = Random()
    rand.seed(time.time())
    return ''.join(rand.sample(VALUES, 8))


def random_seeded_phrase(seed):
    adjs = init_db('adjectives.db')
    nouns = init_db('nouns.db')

    rand = Random()
    rand.seed(seed)
    adj = rand.choice(adjs)
    noun = rand.choice(nouns)

    return "%s %s"%(adj.strip(), noun.strip())


if __name__ in "__main__":
    print random_phrase()
