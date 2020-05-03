# 
# import numpy as np

import pandas as pd
import librosa as lbr        # for importing audio
import imageio as img        # for importing images

class Load:  

    def __init__(self, pathToIndex):
        index = pd.read_csv(pathToIndex + '/index.csv')
        self.path = pathToIndex
        self.index = index
        self.cache = {}
    
    def image(self, key):
        row = self.index[self.index['KEY'] == key]
        ID = row['ID'].iloc[0]
        KEY = row['KEY'].iloc[0]
        loaded = self.isLoaded(KEY)
        if loaded:
            print('Retrieving ' + key + ' from cache')
            data = self.cache[KEY]
        else:
            filePath = self.path + '/' + ID 
            print('Loading ' + filePath)
            data = img.imread(filePath)
            self.toCache(KEY, data)   
        
        print() # add spacing
        
        return data
    
    def audio(self, key, visual = False):
        row = self.index[self.index['KEY'] == key]
        ID = row['ID'].iloc[0]
        KEY = row['KEY'].iloc[0]
        loaded = self.isLoaded(KEY)
        if loaded:
            print('Retrieving ' + key + ' from cache')
            data = self.cache[KEY]
        else:
            audioPath = self.path + '/' + ID 
            print('Loading ' + audioPath)
            data = lbr.load(audioPath)
            self.toCache(KEY, data)        
    
        if visual:
            print(data)
            
        return data
    
    def getID(self,KEY):
        if KEY in self.getKEYs():
            return self.index[self.index['KEY'] == KEY]['ID'].iloc[0]
        
    def getKEY(self,ID):
        if ID in self.getIDs():
            return self.index[self.index['ID'] == ID]['KEY'].iloc[0]
        
    def getIDs(self):
        return self.index['ID'].array
    
    def getKEYs(self):
        return self.index['KEY'].array

    def cacheKEYs(self):
        return self.cache.keys()
        
    def isLoaded(self,key):
        if key in self.cacheKEYs():
            return True
        else:
            return False
        
    def toCache(self,key,data):
        self.cache[key] = data


load = Load('assets')
        
