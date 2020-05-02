import numpy as np
import matplotlib.pyplot as plt

class Display:
        
    def audio(
        self,
        data,
        Fs,
        title="Audio",
        maxAmp = 0,
        ticks = 20, 
        figsize = (18, 4)
    ):
        
        
        t0 = 0
        xLabel = 'Time [s]'
        yLabel = 'Amplitude'
        N = len(data)
        duration = (1/Fs)*N
        time = np.linspace(t0,duration,N)
        
        # calculate shown second marks
        step = (duration - t0)/ticks
            
        plt.figure(figsize=figsize)
        plt.plot(time,data)
        plt.title(title)
        plt.ylabel(yLabel)
        plt.xlabel(xLabel)
        plt.xticks(np.arange(t0, duration, step=step))
        
        if maxAmp > 0:
            plt.ylim((maxAmp, -maxAmp)) 
    

    # Receives a matrix whose elements are real numbers
    # Displays a grayscale image
    # Returns the same matrix but with values between [0,1]
    
    # show parameter is used because there might be some cases
    # in which we only want the value return from
    # plt.imshow for animation purposes but we don't want
    # to waste resources in plotting each matrix individually
    def matrix(self, m, show = True, blend = False):
        
        interpolation = 'nearest'
        
        if blend:
            interpolation = 'bicubic'
            
        
        im = plt.imshow(m, cmap='gray', vmin=0, vmax=1, interpolation=interpolation)
        
        if show:
            plt.show()
        
        return im
        

        
    
disp = Display()