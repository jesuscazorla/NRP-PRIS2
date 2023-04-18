from ast import List
from DataFrame import Dataframe
from Requirement import Requirement
from Stakeholder import Stakeholder
import numpy as np

class NRP (object):
    effortlimit = 0
    requirements = []
    stakeholders = []
    sprint = []
    def __new__(cls):
        return super().__new__(cls)
    
    def setDataframe(self, dataframe: Dataframe):
        self.dataframe = dataframe.df
       
    def printDataframe(self):
        print(self.dataframe)
        
    def translateDataframe(self):
        aux = self.dataframe.to_numpy()
        self.effortlimit = int(aux[0][0])
        for row in aux:
            list = row[2]
            stakeholder = Stakeholder()
            stakeholder.name = list[0]
            stakeholder.requirementInfluence = list[1]
            stakeholder.stakeholderInfluence = row[3]
            stakeholder.influence = 0
            self.stakeholders.append(stakeholder)
            if str(row[1]) != 'nan':
                newR = row[1]
                requirement = Requirement()
                requirement.description = newR[0]
                requirement.effort = newR[1]
                self.requirements.append(requirement)
    def calculateFunctions(self):
        for i in range(len(self.stakeholders)):
            aux = Stakeholder()
            aux.name = self.stakeholders[i].name
            aux.requirementInfluence = self.stakeholders[i].requirementInfluence
            aux.stakeholderInfluence = self.stakeholders[i].stakeholderInfluence
            aux.calculateInfluence(self.stakeholders, i)
            self.stakeholders[i] = aux
        for j in range(len(self.requirements)):
            aux = Requirement()
            aux.description = self.requirements[j].description
            aux.effort = self.requirements[j].effort
            aux.calculateSatisfaction(self.stakeholders, j)
            self.requirements[j] = aux
    def calculateNextSprint(self):
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
            auxLimit -= self.requirements[index].effort
            self.sprint.append(self.requirements.pop(index))
    def printSprint(self):
        for requirement in self.sprint:
            print(requirement.description)