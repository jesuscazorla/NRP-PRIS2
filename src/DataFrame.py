import pandas as pd
import numpy as npppi

from Requirement import Dependency

class Dataframe(object):
    
    effortlimit = pd.DataFrame({'effortLimit':[(10)]})
    requirements = pd.DataFrame({'requirements': [['R1', 4, [Dependency.NONE.name,Dependency.IMPLICACION.name, Dependency.EXCLUSION.name, Dependency.NONE.name, Dependency.EXCLUSION.name]],
                                                  ['R2', 3, [Dependency.IMPLICACION.name,Dependency.NONE.name, Dependency.NONE.name, Dependency.NONE.name, Dependency.NONE.name]], 
                                                  ['R3', 4, [Dependency.EXCLUSION.name,Dependency.INCLUSION.name, Dependency.NONE.name, Dependency.NONE.name, Dependency.NONE.name]],
                                                  ['R4', 3, [Dependency.NONE.name, Dependency.INCLUSION.name, Dependency.NONE.name, Dependency.NONE.name, Dependency.NONE.name]],
                                                  ['R5', 5, [Dependency.EXCLUSION.name, Dependency.NONE.name,Dependency.NONE.name, Dependency.IMPLICACION.name, Dependency.NONE.name]]]})
    stakeholders = pd.DataFrame({'stakeholders': [['John', [False, True, True, True, False]], 
                                                  ['Joe', [True, True, True, True, True]],
                                                  ['Charles', [False, False, False, False, True]],
                                                  ['Paco', [True, True, True,False, False]]]})
    
    stakeholders_relations= pd.DataFrame({'stkh_relation': [[False, False, True,True],
                                                           [False, False, True,False],
                                                           [True, True, False, True],
                                                           [True, True, False, False]]})

    df = pd.concat([effortlimit,requirements,stakeholders,stakeholders_relations], ignore_index=True, axis=1)
    
    def __new__(cls):
        return super().__new__(cls)
   
  
 