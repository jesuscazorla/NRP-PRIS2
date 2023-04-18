class Requirement (object):
    
    description = ''
    effort = 0
    satisfaction = 0
    def __new__(cls):
        return super().__new__(cls) 
    def calculateSatisfaction(self, stakeholders, index):
        for i in range(len(stakeholders)):
            if stakeholders[i].requirementInfluence[index]:
                self.satisfaction += stakeholders[i].influence