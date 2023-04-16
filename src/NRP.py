from ast import List
from DataFrame import Dataframe
from Requirement import Requirement


class NRP (object):
    effortlimit = 0
    requirements = [Requirement]
    stakeholders = []
    
    def __new__(cls):
        return super().__new__(cls)
    
    def setDataframe(self, dataframe: Dataframe):
        self.dataframe = dataframe.df
       
    def printDataframe(self):
        print(self.dataframe)

        
    def translateDataframe(self):
        aux = self.dataframe.to_numpy()
        self.effortlimit = int(aux[0][0])
        #print(self.effortlimit)
        for row in aux:
            list = row[1]
         
            a = str(list) 
            b = a[0]   
            print(b)
            #desc = list[0]
            #eff = list[1]
            requirement = Requirement()
            #requirement.description = desc
            #requirement.effort = eff
            self.requirements.append(requirement)
  
            
       
            
        
        
    
    
