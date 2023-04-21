from ast import List
from DataFrame import Dataframe
from Requirement import Dependency, Requirement
from Stakeholder import Stakeholder
import numpy as np

class NRP (object):
    effortlimit = 0
    requirements = []
    stakeholders = []
    sprint = []
    def __new__(cls):
        return super().__new__(cls)
    
    def setdataframe(self, dataframe: Dataframe):
        self.dataframe = dataframe.df
       
    def printdataframe(self):
        print(self.dataframe)
        
    def translatedataframe(self):
        aux = self.dataframe.to_numpy()
        self.effortlimit = int(aux[0][0])
        for row in aux:
            stake = row[2]
            stakeholder = Stakeholder()
            stakeholder.name = stake[0]
            stakeholder.requirementinfluence = stake[1]
            stakeholder.stakeholderinfluence = row[3]
            stakeholder.influence = 0
            self.stakeholders.append(stakeholder)
            if str(row[1]) != 'nan':
                newR = row[1]
                requirement = Requirement()
                requirement.description = newR[0]
                requirement.effort = newR[1]                    
                requirement.dependencies = newR[2]
                self.requirements.append(requirement)
    def calculatefunctions(self):
        for i in range(len(self.stakeholders)):
            aux = Stakeholder()
            aux.name = self.stakeholders[i].name
            aux.requirementinfluence = self.stakeholders[i].requirementinfluence
            aux.stakeholderinfluence = self.stakeholders[i].stakeholderinfluence
            aux.calculateinfluence(self.stakeholders, i)
            self.stakeholders[i] = aux
        for j in range(len(self.requirements)):
            aux = Requirement()
            aux.description = self.requirements[j].description
            aux.effort = self.requirements[j].effort
            aux.dependencies = self.requirements[j].dependencies
            aux.calculatesatisfaction(self.stakeholders, j)
            self.requirements[j] = aux
            
    def calculatenextsprint(self):
        auxlimit = self.effortlimit
        while len(self.requirements) > 0:
            index = -1            
            bestrequirement = self.chooserequirement(auxlimit)
            index = bestrequirement[1]
                                
            if index == -1:
                break
            else:
                implicationresult = self.checkimplication(index, auxlimit)
                if implicationresult[0] == 0:
                    for i in range (len(implicationresult[1])):
                        for j in reversed(range(len(self.requirements))):
                            self.requirements[j].dependencies.pop(i)
                            self.requirements.pop(implicationresult[1][i]-i)
                    continue  
                else:
                    if len(implicationresult[1]) == 1:   
                      auxlimit -= self.requirements[index].effort
                    else:
                        auxlimit -= implicationresult[0]
                        for j in reversed(range (len(implicationresult[1]))):
                            self.sprint.append(self.requirements.pop(j))
                        self.sprint.reverse()
                        continue                  
               
            newindex = index
            exclusionchecked = self.checkexclusion(index, newindex)
            newindex = exclusionchecked[0]       
            removed = exclusionchecked[1]
                    
            for i in range(len(removed)):
                for j in range(len(self.requirements)):
                    self.requirements[j].dependencies.pop(i)
                self.requirements.pop(removed[i]-i)
            
            self.sprint.append(self.requirements.pop(newindex))
            for i in range(len(self.requirements)):
                self.requirements[i].dependencies.pop(newindex) 
    
    def checkimplication(self, index, auxlimit):
        effort = self.requirements[index].effort
        implicacion = [index]
        for i in range(len(self.requirements[index].dependencies)):
            if self.requirements[index].dependencies[i] == 'IMPLICACION' and i !=index:
                effort += self.requirements[i].effort
                implicacion.append(i)      
       
 
        
        if(effort <= auxlimit):
              return [effort, implicacion]
        else: 
              return [0, implicacion]           
          
    def chooserequirement(self, auxlimit):
        indx = -1
        maxsat = 0
        for i in range(len(self.requirements)):
            if(self.requirements[i].effort <= auxlimit and self.requirements[i].satisfaction > maxsat):
                maxsat = self.requirements[i].satisfaction
                indx = i
        return [maxsat, indx]
    
    def checkexclusion(self,index,newindex):
        remove = []
        for i in range(len(self.requirements[index].dependencies)):
            if self.requirements[index].dependencies[i] == 'EXCLUSION' and i != index:
                remove.append(i)
                if i < index:
                    newindex = newindex-1 
        
        return [newindex,remove]
                    
        
    def printSprint(self):
        print("Los requisitos a realizar para el proximo sprint son:")
        print("El limite de esfuerzo es de %s" % (self.effortlimit))
        effortused = 0
        if(len(self.sprint) == 0):
            print("Check Dataframe....imposible to find at least one requirement for this sprint")
        else:
            for requirement in self.sprint:      
                effortused += requirement.effort
                print("Description: %s Satisfaction: %s Effort: %s" % (requirement.description,requirement.satisfaction,requirement.effort))
            print("Effort used: %s" % (effortused))    
            
            
