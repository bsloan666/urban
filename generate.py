#!/usr/bin/env python
import sys
import os
import re
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
    adjs =  init_db('adjectives.db')
    nouns = init_db('nouns.db')

    shuffle(adjs)
    shuffle(nouns)

    a_range = range(len(adjs))
    n_range = range(len(nouns))

    shuffle(a_range)
    shuffle(n_range)

    tmp =  nouns[n_range[0]].strip()
    noun,alt_noun = re.split('\|', tmp)
    tmp =  adjs[a_range[0]].strip()
    adj,alt_adj = re.split('\|', tmp)

    return (adj, alt_adj, noun, alt_noun)

def random_phrase_2():
    show_adjs =  init_db('adj.show.db')
    show_nouns = init_db('noun.show.db')

    hide_adjs =  init_db('adj.hide.db')
    hide_nouns = init_db('noun.hide.db')

    sa_range = range(len(show_adjs))
    sn_range = range(len(show_nouns))
    ha_range = range(len(hide_adjs))
    hn_range = range(len(hide_nouns))

    shuffle(sa_range)
    shuffle(sn_range)
    shuffle(ha_range)
    shuffle(hn_range)

    noun =      show_nouns[sn_range[0]].strip()
    alt_noun =  hide_nouns[hn_range[0]].strip()
    adj =       show_adjs[sa_range[0]].strip()
    alt_adj =   hide_adjs[ha_range[0]].strip()

    return (adj, alt_adj, noun, alt_noun)


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
    (a,c,b,d) = random_phrase_2() 
    print "%s %s (%s %s)"%(a,b,c,d)
