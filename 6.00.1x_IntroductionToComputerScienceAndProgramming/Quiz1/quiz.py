def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

def myLog(x, b):
    exp = 0
    while (b**exp < x):
        exp += 1
    if b**exp == x:
        return exp
    return exp - 1

assert (4 == myLog(16, 2))
assert (2 == myLog(15, 3))

def laceStrings(s1, s2):
    if (len(s1) > len(s2)):
        max = len(s1)
    else:
        max = len(s2)
    result = ''
    for idx in range(max):
        if(idx < len(s1)):
            result += s1[idx]
        if(idx < len(s2)):
            result += s2[idx]
    return result

assert('' == laceStrings('',''))
assert('abc' == laceStrings('abc',''))
assert('abc' == laceStrings('','abc'))
assert('aebfcgdhi' == laceStrings('abcd','efghi'))

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:],s2[1:],out + s1[0] + s2[0]) 
    return helpLaceStrings(s1, s2, '')


assert('' == laceStringsRecur('',''))
assert('abc' == laceStringsRecur('abc',''))
assert('abc' == laceStringsRecur('','abc'))
assert('aebfcgdhi' == laceStringsRecur('abcd','efghi'))

def McNuggets(n):
    if (n < 0):
        return False
    if (n%6 == 0 or n%9 == 0 or n%20 == 0):
        return True
    return McNuggets(n - 6) or McNuggets(n - 9) or McNuggets(n - 20)

assert (True == McNuggets(6))
assert (True == McNuggets(9))
assert (True == McNuggets(15))
assert (False == McNuggets(16))

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(10000):
        print "f(guess) is", f(guess),  "guess is", guess 
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            print "guess is", guess, ",f(guess) is ", f(guess)
            guess = f(guess)
    return guess

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)

print sqrt(10)
