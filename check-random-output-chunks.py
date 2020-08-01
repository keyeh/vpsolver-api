import sys
import random
from all_hands_analysis import all_hands_gen, hand2str
from all_hands_analysis import handResultToByte
from vp_analyzer import HandAnalyzer, DiscardValue

all_hands_str_l = list(map(hand2str, all_hands_gen()))

def getHandStringAt(i):
    return all_hands_str_l[i]

lutBytes = []

with open("job-9-6 2.bin", "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        lutBytes.append(byte)


def makeStringFromByte(byte):
    int_value = ord(byte)
    binary_string = '{0:08b}'.format(int_value)
    # print(binary_string)
    return binary_string

def makeStringFromInt(int_value):
    binary_string = '{0:08b}'.format(int_value)
    # print(binary_string)
    return binary_string


if __name__ == '__main__':
    for k in range(52):
        chunkSize = 49980
        i = random.randint(k*chunkSize, k*chunkSize + chunkSize)
        # i=k

        handStr = getHandStringAt(i)
        lutByteString = makeStringFromByte(lutBytes[i])
        
        analysis = HandAnalyzer(handStr).analyze(return_full_analysis=False, return_bestdisc_cnts = False)
        analysisByteString = makeStringFromInt(handResultToByte(analysis[0]))
        # if(k % 100 == 0):
        print(i)
        if(lutByteString != analysisByteString):
            print("FAILED")
            print(i)
            print(handStr)
            print(lutByteString)
            print(analysisByteString)
            exit()
    print("PASS")
