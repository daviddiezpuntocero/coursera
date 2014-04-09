def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def cV(X):
    mean = sum(X)/float(len(X))
    return stdDev(X)/mean


print cV([10,4,12,15,20,5])

