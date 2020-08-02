import sys
from collections import Counter
from itertools import combinations, product
from all_hands_analysis import all_hands_gen, hand2str
from scipy.special import comb
from deck import deck

def makeStringFromByte(byte):
    int_value = ord(byte)
    binary_string = '{0:08b}'.format(int_value)
    # print(binary_string)
    return binary_string

def handStringToIntArray(handStr):
    n = 2
    a = [handStr[i:i+n] for i in range(0, len(handStr), n)]
    a = map(cardToNumber, a)
    return a

def intArrayToHand(ints):
    return map(numberToCard,ints)

def numberToCard(n):
    return deck[n-1]
def cardToNumber(card):
    return deck.index(card) + 1

def nck(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

def find_idx(comb,n):
    k=len(comb)
    idx=0
    last_c=0
    for c in comb:
        #idx+=sum(nck(n-2-x,k-1) for x in range(c-last_c-1)) # a little faster without nck caching
        idx+=nck(n-1,k)-nck(n-c+last_c,k) # more elegant (thanks to Ray), faster with nck caching
        n-=c-last_c
        k-=1
        last_c=c
    return idx


if __name__ == '__main__':
    handString = sys.argv[1]
    handIntArray = handStringToIntArray(handString)
    print(handIntArray)

    result = find_idx(handIntArray, 53)
    print(result)

    lutBytes = []
    with open("job-9-6.bin", "rb") as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            lutBytes.append(byte)
    
    byte = lutBytes[result]
    print(makeStringFromByte(byte))
