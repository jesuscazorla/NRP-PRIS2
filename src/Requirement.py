class Requirement (object):
    
    description = ''
    effort = 0
    
    def __new__(cls):
        return super().__new__(cls)
        
    #def __init__(self, effort, description):
    #    self.effort = effort
    #    self.description = description
    def calculateSatisfaction(stakeholders, self, index):
        for i in range(len(stakeholders)):
            if stakeholders[i].requirementInfluence[index]:
                self.satisfaction = stakeholders[i].influence