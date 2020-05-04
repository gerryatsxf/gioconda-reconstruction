import numpy as np
import tools.vertices as vpr
from tools.blend import blend


def generateRandomDna(dnaLength,m,n):
#     dnaLength is the number of columns the dna matrix is going to have.
#     first generate a random [0,1] interval matrix of 2 x dnaLength for the top of the matrix. This will be the random gray and alpha index.
    grayAndAlpha = np.random.rand(1,dnaLength)
    
#     then generate a random matrix in the [0,m-1] and [0,n-1] intervals for the vertices of the triangles
    multipleLongRandomPolygonVertices = vpr.multipleRandomLongPolygonVertices(m,n,dnaLength)
    
    randomDna = np.concatenate((grayAndAlpha, multipleLongRandomPolygonVertices), axis=0)
    
    return randomDna

def merge(dna,population,m,n):
    (p,q) = population.shape
    populationDna = np.zeros((m,n))
    for k in range(q):
        currentIndividual = population[:,k]
        dnaCopy = np.array(dna, copy=True)
        currentDna = mergeIndividualOnDna(dnaCopy,currentIndividual,m,n)
        populationDna = np.dstack((populationDna,currentDna))
        
    return populationDna[:,:,1:]
        

def mergeIndividualOnDna(dna,individual,m,n):
    G = individual[0]
    longXY = individual[1:]
    polygon = vpr.booleanPolygon(m, n, longXY, long = True)*G
    return blend.matrices(polygon,dna)
    

def randomPop(popSize,m,n):
    gray = np.random.rand(1,popSize)
    
#     then generate a random matrix in the [0,m-1] and [0,n-1] intervals for the vertices of the triangles
    multipleLongRandomPolygonVertices = vpr.multipleRandomLongPolygonVertices(m,n,popSize)
    
    randomPop = np.concatenate((gray, multipleLongRandomPolygonVertices), axis=0)
    
    return randomPop
    