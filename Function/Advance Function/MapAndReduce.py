# map(f,iterable) returns an interator
# reduce(f,in)

from functools import reduce

def char2num(c):
    charNums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return charNums[c]

def combine(x, y):
    return x*10 + y

def str2num(str):
    return reduce(combine,map(char2num,str))
