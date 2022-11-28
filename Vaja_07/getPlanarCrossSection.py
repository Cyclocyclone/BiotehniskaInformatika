import numpy as np
import sys


def getPlanarCrossSection(iImage, iNormVec, iLoc):

    oCS = []
    if iNormVec == [1, 0, 0]:
        oCS = np.squeeze(iImage[:, iLoc, :])

    elif iNormVec == [0, 1, 0]:
        oCS = np.squeeze(iImage[iLoc, :, :])

    elif iNormVec == [0, 0, 1]:
        oCS = np.squeeze(iImage[:, :, iLoc])
    else:
        sys.exit("Error")
    return oCS