# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for
    delays of 300, 150, 75, 0 timesteps (followed by an additional 150
    timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)

    """
    timestep = 300
    population = []
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    for i in range(timestep):
        population.insert(i, 0)

    rsp = []
    for i in range(timestep):
        rsp.insert(i, 0)

    for nt in range(numTrials):

        viruses = []
        for i in range(numViruses):
            virus = ResistantVirus(maxBirthProb, clearProb,
                                   resistances, mutProb)
            viruses.append(virus)

        patient = TreatedPatient(viruses, maxPop)
        for t in range(timestep/2):
            population[t] += float(patient.update())
            rsp[t] += float(patient.getResistPop(["guttagonol"]))

        patient.addPrescription("guttagonol")

        for t in range(timestep/2, timestep):
            population[t] += float(patient.update())
            rsp[t] += float(patient.getResistPop(["guttagonol"]))

    for i in range(timestep):
        population[i] = population[i]/numTrials
        rsp[i] = rsp[i]/numTrials
    pylab.hist(population, bins=50)
    pylab.title('Population')
    pylab.xlabel('Population')
    pylab.ylabel('Number of trials')
    pylab.show()

simulationDelayedTreatment(20)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
