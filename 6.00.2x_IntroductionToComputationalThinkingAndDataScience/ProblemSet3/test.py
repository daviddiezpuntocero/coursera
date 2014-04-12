from ps3b_precompiled_27 import *

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    population = []
    for i in range(300):
        population.insert(i, 0)
    for i in range(numTrials):
        viruses = []
        for i in range(numViruses):
            viruses.append(SimpleVirus(maxBirthProb, clearProb))
        patient = Patient(viruses, maxPop)
        for t in range(300):
            population[t] += float(patient.update())
    for i in range(300):
        population[i] = population[i]/numTrials
    pylab.plot(range(300), population)
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(('Population', 'Time'))
    pylab.show()
 
simulationWithoutDrug(100, 1000, 0.1, 0.05, 20)
