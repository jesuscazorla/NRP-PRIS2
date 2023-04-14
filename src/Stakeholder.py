class Stakeholder:
    
    def __init__(self, name, requirementInfluence, stakeholderInfluence):
        self.name = name
        self.requirementInfluence = requirementInfluence
        self.stakeholderInfluence = stakeholderInfluence
        
    def calculateInfluence(stakeholders, self):
        for i in range(len(stakeholders)):
            for j in range(len(stakeholders[i].stakeholderInfluence)):
                if(i != j):
                    if(stakeholders[i].stakeholderInfluence[j] == True):
                        self.influence += 1   