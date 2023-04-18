from enum import Enum

class Dependency(Enum):
    INCLUSION = 1
    EXCLUSION = 2
    IMPLICACION = 3
    NONE = 4

class Requirement (object):
    
    description = ''
    effort = 0
    satisfaction = 0
    dependencies = []
    def __new__(cls):
        return super().__new__(cls) 
    
    def setDependencies(self, dependencies):
        self.dependencies = dependencies
        
    def calculateSatisfaction(self, stakeholders, index):
        for i in range(len(stakeholders)):
            if stakeholders[i].requirementinfluence[index]:
                self.satisfaction += stakeholders[i].influence
                