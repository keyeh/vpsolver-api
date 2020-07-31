import sys
from itertools import combinations, product
import os.path
from os import path

def all_hands_gen():
    ranks = 'A23456789TJQK'
    suits = 'cdhs'

    deck = product(ranks, suits)
    return combinations(deck, 5)


def hand2str(hand_tup):
    hstr = ''
    for r, s in hand_tup:
        hstr += r + s
    return hstr

all_hands_str_l = list(map(hand2str, all_hands_gen()))


if __name__ == '__main__':
    i = int(sys.argv[1])
    print(i)
    print(all_hands_str_l[i])
