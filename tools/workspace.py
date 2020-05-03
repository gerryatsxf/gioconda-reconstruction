# make a persistent workspace class

# it will make use to check (with a keyword) if there is an
# existent workspace available. if there is, it loads the storaged
# variables. if it isn't, it will return freshly initialized variables


# it will have a method named save. it will receive as parameters 
# evolution
# optional keywork


# the received evolution will be stored in .pkl file. maybe a checkup will be necessary? like
# first check out the amount of DNAs inside evolution. if it's less than last time, launch
# a user input requesting an informed confirmation. 

# also check out dimensions of DNA. if dimensions are not the same then it is
# pretty much obvious that we are not talking about the same image.

import os.path
import pickle

class Workspace:
    
    def __init__(self, folderPath):
        self.folderPath = folderPath
    
    # controlImg is asked so that bestFitness can be calculated because
    # evolution doesn't keep a harcoded record of the fitnesses
    def evolution(self,keyword):
        basePath = self.folderPath + '/' + keyword
        pklPath = basePath + '.pkl'

        # existent: boolean -> indicates if pkl file exists or not
        existent = self.stageFile(pklPath)
        
        ev = [];
        
        if existent:
            with open(pklPath, 'rb') as file: 
                ev = pickle.load(file)
        else:
            print("No file created.")
            print()
            
        if len(ev) == 0:
            print("Returning an empty evolution.")
            print()
        else:
            (m,n) = ev[0].shape
            print('Image size: (' + str(m) + ',' + str(n) + ')')
            print('Evolution length: ' + str(len(ev)))
            print()
            
        return ev

    # checks if file exists
    # if it does, returns True
    # if it doesn't, it asks the user if she wants to create one
    # if she does, return True
    # else, return False
    def stageFile(self,pklPath):
        
        # initialize create confirmation response 
        isExistent = False
        
        try:
            
            if os.path.isfile(pklPath):

                msg = "File '" + pklPath + "' exist. Workspace will be loaded."
                print(msg)
                print()
                isExistent = True

            else:

                msg = "File '" + pklPath + "' does not exist."
                raise Exception("inexistent",msg)
                
        except Exception as inst:
            
            if inst.args[0] == "inexistent":
                
                # show problem message to user
                print(inst.args[1])
                print()
                
                # response is empty string if there's no user input
                response = input("Do you want to create a new .pkl file for this Workspace? [Y/n]: ") 
                print()
                
                # handle response
                if response == 'y' or response == 'Y' or response == '':
                    msg = "Creating file '" + pklPath + "'"
                    print(msg)
                    self.dump(pklPath,[])
                    isExistent = True
                elif response == 'n':
                    msg = "Thanks for coming, have a nice day."
                    print(msg)
                print() # spacing for next print
                
        return isExistent
                    
        
        
#     def getFile(plkPath):

            
            
            
    def dump(self,pklPath,evolution):
        with open(pklPath, 'wb') as file: 
            pickle.dump(evolution, file) 
                    

                
                
                
                
                
                
                
# # save progress
# import pickle

# # .pkl file path constructon
# folderPath = 'storage/'
# filePath = folderPath + keyword + '.pkl'

# # uncomment if you want to load progress
# with open(filePath, 'rb') as file: 
#     evolution = pickle.load(file)
    
                
                
                
                
                
                
                
                
ws = Workspace('workspace')