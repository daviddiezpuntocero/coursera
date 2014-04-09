import math
def stdDevOfLengths(L):
    if(len(L) == 0):
        return float('NaN')
    lens = []
    for s in L:
        lens.append(len(s))
    mean = (sum(lens)/float(len(lens)))
    ss = 0.0
    for l in lens:
        ss += (l - mean) * (l - mean)
    return (ss / len(lens))**0.5

assert(stdDevOfLengths(['a','z','p']) == 0) 
assert(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']) == 1.8708) 
