import sys
from all_hands_analysis import all_hands_gen, hand2str
import os.path
from os import path

all_hands_str_l = list(map(hand2str, all_hands_gen()))


f=open('all_hands.txt','w')
for ele in all_hands_str_l:
    f.write(ele+'\n')

f.close()
