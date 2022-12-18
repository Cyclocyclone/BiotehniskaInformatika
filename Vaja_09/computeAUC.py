import numpy as np

def computeAUC(iX, iY):
    AUC = np.trapz(iY, x=iX)
    AUC = np.absolute(AUC)
    AUC = np.around(AUC, 3)
    return AUC