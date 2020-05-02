class Processor:
    
    
    # Argument matrix is a numpy array of two dimensions
    def maxscale(self, matrix):
        
        maxVal = matrix.max()
        return matrix/maxVal
        
        
        
proc = Processor()