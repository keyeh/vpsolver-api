import sys
from all_hands_analysis import all_hands_gen, hand2str
import os.path
from os import path
import json

with open('deck.json') as f:
  cardToNumber = json.load(f)

def toNumber(cardStr):
    return(cardToNumber[cardStr])


def hand2str(hand_tup):
    hstr = ''
    for r, s in hand_tup:
        n = toNumber(r + s)
        hstr += str(n).zfill(2)
    return hstr

all_hands_str_l = list(map(hand2str, all_hands_gen()))


f=open('all_hands.txt','w')
for ele in all_hands_str_l:
    f.write(ele+'\n')

f.close()
