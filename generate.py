#!/usr/bin/env python

"""
Generate a random NP
"""
import re
import time
import string
from random import shuffle, Random

VALUES = string.ascii_letters + string.digits


def init_db(fname):
    """
    Given a file path, initialize the database
    """
    handle = open(fname, 'r')
    lines = handle.readlines()
    handle.close()
    return lines


def random_phrase():
    """
    One from column A one from column B
    """
    adjs = init_db('adjectives.db')
    nouns = init_db('nouns.db')

    shuffle(adjs)
    shuffle(nouns)

    a_range = range(len(adjs))
    n_range = range(len(nouns))

    shuffle(a_range)
    shuffle(n_range)

    tmp = nouns[n_range[0]].strip()
    noun, alt_noun = re.split(r'\|', tmp)
    tmp = adjs[a_range[0]].strip()
    adj, alt_adj = re.split(r'\|', tmp)

    return (adj, alt_adj, noun, alt_noun)


def random_phrase_2():
    """
    Is this one somehow better?
    """
    show_adjs = init_db('adj.show.db')
    show_nouns = init_db('noun.show.db')

    hide_adjs = init_db('adj.hide.db')
    hide_nouns = init_db('noun.hide.db')

    rand = Random()

    rand.seed(int(time.time())%7390571)

    noun = rand.choice(show_nouns).strip()
    alt_noun = rand.choice(hide_nouns).strip()
    adj = rand.choice(show_adjs).strip()
    alt_adj = rand.choice(hide_adjs).strip()

    return (adj, alt_adj, noun, alt_noun)


def random_seed():
    """
    Use time to make random more random
    """
    rand = Random()
    rand.seed(time.time())
    return ''.join(rand.sample(VALUES, 8))


def random_seeded_phrase(seed):
    """
    Er. Wut?
    """
    adjs = init_db('adjectives.db')
    nouns = init_db('nouns.db')

    rand = Random()
    rand.seed(seed)
    adj = rand.choice(adjs)
    noun = rand.choice(nouns)

    return "%s %s"%(adj.strip(), noun.strip())


if __name__ in "__main__":
    (a, c, b, d) = random_phrase_2()
    print("%s %s (%s %s)"%(a, b, c, d))
