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
            aux.calculateInfluence(self.stakeholders, i)
            self.stakeholders[i] = aux
        for j in range(len(self.requirements)):
            aux = Requirement()
            aux.description = self.requirements[j].description
            aux.effort = self.requirements[j].effort
            aux.dependencies = self.requirements[j].dependencies
            aux.calculateSatisfaction(self.stakeholders, j)
            self.requirements[j] = aux
    def calculatenextsprint(self):
        auxLimit = self.effortlimit
        while len(self.requirements) > 0:
            maxSatisfaction = 0
            index = -1
            more = False
            for requirement in self.requirements:
                if requirement.effort <= auxLimit:
                    more = True
            if more == False:
                break
            for i in range(len(self.requirements)):
                if(self.requirements[i].effort <= auxLimit and self.requirements[i].satisfaction > maxSatisfaction):
                    maxSatisfaction = self.requirements[i].satisfaction
                    index = i
                    #exclusionDependencies = np.where(self.requirements[i].dependencies==Dependency.EXCLUSION)
                    #if(exclusionDependencies.count != 0):
                    #    for i in exclusionDependencies:
                    #      self.requirements.pop(exclusionindex)
                
                            
            auxLimit -= self.requirements[index].effort
            self.sprint.append(self.requirements.pop(index))
    def printSprint(self):
        print("Los requisitos a realizar para el proximo sprint son:")
        print("El limite de esfuerzo es de %s" % (self.effortlimit))
        effortused = 0
        for requirement in self.sprint:         
            effortused += requirement.effort
            print("Description: %s Satisfaction: %s Effort: %s" % (requirement.description,requirement.satisfaction,requirement.effort))