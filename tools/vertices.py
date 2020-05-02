import numpy as np
import numpy.random as rand
import tools.triangles as trr


def repeatedVertices(XY):
    return np.array_equal(XY[0,:],XY[1,:]) or np.array_equal(XY[1,:],XY[2,:]) or np.array_equal(XY[2,:],XY[0,:])


def randomPolygonVertices(m,n):
    
    while True:
#         Return random integers from low (inclusive) to high (exclusive).
#         size : int or tuple of ints, optional
        X = rand.randint(low=0,high=m, size=(3,1))
        Y = rand.randint(low=0,high=n, size=(3,1))

        XY = np.column_stack((X,Y))
        
        if ~repeatedVertices(XY):
            break

    return XY

def booleanPolygon(m, n, XY, long = False):
    if long == True:
        XY.shape = (3,2)
    bMatrix = np.zeros((m,n))
    XY = XY.astype(int)
    bMatrix = trr.drawTriangle(bMatrix, XY)
    return bMatrix

def randomPolygon(m,n):
    XY = randomPolygonVertices(m,n)
    return booleanPolygon(m, n, XY, long = False)

def multipleRandomLongPolygonVertices(m,n,N):
    
#     longPolygonVertices is a 6xN matrix
    multipleLongPolygonVertices = np.zeros((6,1))
    for k in range(N):
        longXY = randomPolygonVertices(m,n)
        longXY.shape = 6
        multipleLongPolygonVertices = np.column_stack((multipleLongPolygonVertices,longXY))
                
    multipleLongPolygonVertices = multipleLongPolygonVertices[:,1:]
    return multipleLongPolygonVertices

        
        
def multipleLongVerticesToPolygons(longXYs,m,n):
    
    numVertices = longXYs.shape[1]
    
    multiplePolygons = np.zeros((m,n))
    # lets iterate trhough all columns
    for k in range(numVertices):
        longXY = longXYs[:,k]

        currentPolygon = booleanPolygon(m, n, longXY, long = True)
        multiplePolygons = np.dstack((multiplePolygons, currentPolygon))
        
    return multiplePolygons[:,:,1:]