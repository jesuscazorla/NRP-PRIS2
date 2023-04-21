class Stakeholder:
    
    name = ''
    requirementinfluence = [bool]
    stakeholderinfluence = [bool]
    influence = 0
    def __new__(cls):
        return super().__new__(cls)
    def calculateinfluence(self,stakeholders, index):
        for i in range(len(stakeholders)):
            if(i != index):
                if(stakeholders[i].stakeholderinfluence[index] == True and str(stakeholders[i]) != 'NaN'):
                    self.influence = self.influence+1   