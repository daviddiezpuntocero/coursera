

def genPrimes():
    loop = 0
    while True:
        for i in range(loop/2):
            if loop == 2:
                yield loop
            elif loop % (i+2) == 0:
                break
            elif i + 1 == loop/2:
                yield loop
        loop += 1
