import pandas as pd
import numpy as np

class Dataframe(object):
    
    effortLimit = pd.DataFrame({'effortLimit':[(5)]})
    requirements = pd.DataFrame({'requirements':[['R0', 2],['R1', 1],['R2', 3]]})
    stakeholders = pd.DataFrame({'stakeholders': [['John', [True, False,True]], 
                                                  ['Joe', [False, False,True]],
                                                  ['Charles', [True, True,False]],
                                                  ['Paco', [False, False, False]]]})
    
    stakeholders_relations= pd.DataFrame({'stkh_relation':[[False, False, True,False],
                                                           [True, False, True,False],
                                                           [True, True, False, False],
                                                           [True, True, True, False]]})

    df = pd.concat([effortLimit,requirements,stakeholders,stakeholders_relations], ignore_index=True, axis=1)
    
    def __new__(cls):
        return super().__new__(cls)
   
  
 