def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    times  = 3
    same = 0
    for trial in range(numTrials):
        balls  = ["GREEN", "GREEN", "GREEN", "RED", "RED", "RED"]
        indexs = [0,1,2,3,4,5]
        out = []
        for time in range(times):
            idx = random.choice(range(len(indexs)))
            indexs.pop(idx)
            out.append(balls.pop(idx))
        if out[0] == out[1] == out[2]:
            same += 1
    return float(same) / float(numTrials)    

print noReplacementSimulation(100000)
