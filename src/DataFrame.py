import pandas as pd
import numpy as npppi

from Requirement import Dependency

class Dataframe(object):
    
    effortlimit = pd.DataFrame({'effortLimit':[(5)]})
    requirements = pd.DataFrame({'requirements': [['R0', 2, [Dependency.EXCLUSION.name,Dependency.NONE.name, Dependency.NONE.name]], ['R1', 1, [Dependency.IMPLICACION.name, Dependency.NONE.name,Dependency.NONE.name]], ['R2', 3, [Dependency.IMPLICACION.name,Dependency.NONE.name, Dependency.NONE.name]]]})
    stakeholders = pd.DataFrame({'stakeholders': [['John', [True, True,True]], 
                                                  ['Joe', [False, False,True]],
                                                  ['Charles', [True, True,False]],
                                                  ['Paco', [False, False, False]]]})
    
    stakeholders_relations= pd.DataFrame({'stkh_relation': [[False, False, True,False],
                                                           [True, False, True,False],
                                                           [True, True, False, False],
                                                           [True, True, True, False]]})

    df = pd.concat([effortlimit,requirements,stakeholders,stakeholders_relations], ignore_index=True, axis=1)
    
    def __new__(cls):
        return super().__new__(cls)
   
  
 