from NRP import NRP
from DataFrame import Dataframe

def main():
    dataframeaux = Dataframe()
    nrp = NRP()
    nrp.setdataframe(dataframeaux)
    nrp.translatedataframe()
    nrp.calculatefunctions()
    nrp.printdataframe()
    nrp.calculatenextsprint()
    nrp.printSprint()
if __name__ == "__main__":
    main()