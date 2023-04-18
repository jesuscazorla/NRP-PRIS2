class Stakeholder:
    
    name = ''
    requirementInfluence = [bool]
    stakeholderInfluence = [bool]
    influence = 0
    def __new__(cls):
        return super().__new__(cls)
    def calculateInfluence(self,stakeholders, index):
        for i in range(len(stakeholders)):
            if(i != index):
                if(stakeholders[i].stakeholderInfluence[index] == True):
                    self.influence = self.influence+1   