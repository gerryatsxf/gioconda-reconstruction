
import numpy as np

def fitness(controlImg, testImg):
    res = abs(controlImg-testImg)
    return np.sum(res)


    
def getPopulationDnaFitnesses(populationDna,controlImg):
    
    (m,n,l) = populationDna.shape
    fitnesses = []
    for k in range(l):
        currentIndividualDna  = populationDna[:,:,k]
        currentFitness = fitness(controlImg,currentIndividualDna)
        fitnesses.append(currentFitness)
    
    return fitnesses
    
def orderPopulationDnaByFitness(populationDna,controlImg):
    
    fitnesses = getPopulationDnaFitnesses(populationDna,controlImg)
    
    orderIdx = np.argsort(fitnesses)
    
    (m,n) = populationDna[:,:,0].shape
    
    orderedPopulationDna = np.zeros((m,n))
    orderedFitnesses = []
    
    for idx in orderIdx:
        orderedPopulationDna = np.dstack((orderedPopulationDna,populationDna[:,:,idx]))
        orderedFitnesses.append(fitnesses[idx])
        
    return (orderedFitnesses, orderedPopulationDna[:,:,1:])

