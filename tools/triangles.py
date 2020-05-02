import numpy as np

def drawLine(M,x1,x2,y):
    diff = np.abs(x2 - x1)
    fill = np.ones((1,diff+1))
    if x1 == x2:
        M[y,x1] = fill
    elif x1 < x2:        
        M[y,x1:x2+1] = fill
    else:
        M[y,x2:x1+1] = fill
    return M

def fillTopFlatTriangle(M,v1,v2,v3):
#     parameters:
#         M is the matrix where the triangle is going to be filled
#         v1 first vertex
#         v2 second vertex
#         v3 third vertex
 
#     vertices are 1x2 dimensional array
#     we will always treat this pair of numbers as matrix indices, never as x-y coordinates
    
#     order goes from smallest to biggest
#     vertex must be ordered by their y values (index 0 since it represents a indices of a matrix)
#     if two of them are supposed to have the same y value it doesn't matter which order they are given as long as the third
#     vertex with the "bottomest" y (and thus the greatest row matrix index) goes first (i.e. vertex v1)
    invSlope2 = ( v2[1] - v1[1] ) / ( v2[0] - v1[0] ) # notice this is an inverse slope and thus x components go in the numerator
    invSlope1 = ( v3[1] - v1[1] ) / ( v3[0] - v1[0] ) # notice this is an inverse slope and thus x components go in the numerator

    curx1 = v1[1] # we initialize the x in the same spot, at the top of the triangle
    curx2 = v1[1] # we initialize the x in the same spot, at the top of the triangle

    # we then start filling index by index in the row axis starting from the top tip of the triangle
    rang = np.arange(v1[0],v2[0]+1,1) 
    
    for scanLineY in rang:

        x1 = int(np.round(curx1))
        x2 = int(np.round(curx2))
        
        M = drawLine(M, x1, x2, scanLineY);
        curx1 = curx1+invSlope1;
        curx2 = curx2+invSlope2;
        
    return M
       
def fillBottomFlatTriangle(M,v1,v2,v3):
#     parameters:
#         M is the matrix where the triangle is going to be filled
#         v1 first vertex
#         v2 second vertex
#         v3 third vertex

#     vertices are 1x2 dimensional array
#     we will always treat this pair of numbers as matrix indices, never as x-y coordinates

#     order goes from smallest to biggest
#     vertex must be ordered by their y values (index 0 since it represents a indices of a matrix)
#     if two of them are supposed to have the same y value it doesn't matter which order they are given as long as the third
#     vertex with the "bottomest" y (and thus the greatest row matrix index) goes first (i.e. vertex v1)
    invSlope2 = ( v3[1] - v1[1] ) / ( v3[0] - v1[0] ) # notice this is an inverse slope and thus x components go in the numerator
    invSlope1 = ( v3[1] - v2[1] ) / ( v3[0] - v2[0] ) # notice this is an inverse slope and thus x components go in the numerator

    curx1 = v3[1] # we initialize the x in the same spot, at the bottom of the triangle
    curx2 = v3[1] # we initialize the x in the same spot, at the bottom of the triangle

    # we then start filling index by index in the row axis starting from the bottom tip of the triangle
    rang = np.arange(v3[0],v2[0],-1) 

    for scanLineY in rang:

        x1 = int(np.round(curx1))
        x2 = int(np.round(curx2))
        
        M = drawLine(M, x1, x2, scanLineY);
        curx1 = curx1-invSlope1;
        curx2 = curx2-invSlope2;
        
    return M

def sortVerticesByY(XY):
    # XY is an Nx2 array where N is the number of vertices that we have available
    # the columns represent a pair of indices of a 2-dimensional matrix
    n = 0
    XY = XY[XY[:,n].argsort()]
    return XY

def drawTriangle(M, XY):
    XY = sortVerticesByY(XY);
    M = fillTopFlatTriangle(M, XY[0,:], XY[1,:], XY[2,:]);
    M = fillBottomFlatTriangle(M, XY[0,:], XY[1,:], XY[2,:]);
    return M