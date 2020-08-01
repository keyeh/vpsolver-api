import sys
from all_hands_analysis import all_hands_gen, hand2str
import os.path
from os import path


def getHandStringAt(i):
    all_hands_str_l = list(map(hand2str, all_hands_gen()))
    return all_hands_str_l[i]

if __name__ == '__main__':
    i = int(sys.argv[1])
    print(getHandStringAt(i))
