import sys
from NRP import NRP
from DataFrame import Dataframe

def main():
    args = sys.argv[1:]
    dataframeaux = Dataframe()
    nrp = NRP()
    nrp.setdataframe(dataframeaux)
    if len(args) >= 1 and args[0] == '-showdf':
        nrp.printdataframe()
    nrp.translatedataframe()
    nrp.calculatefunctions()
    
         
    nrp.calculatenextsprint()
    nrp.printsprint()
    
    
if __name__ == "__main__":
    main()