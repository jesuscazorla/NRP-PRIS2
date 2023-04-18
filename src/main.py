from NRP import NRP
from DataFrame import Dataframe

def main():
    dataframeaux = Dataframe()
    nrp = NRP()
    nrp.setDataframe(dataframeaux)
    nrp.translateDataframe()
    nrp.calculateFunctions()
    nrp.printDataframe()
    nrp.calculateNextSprint()
    nrp.printSprint()
if __name__ == "__main__":
    main()