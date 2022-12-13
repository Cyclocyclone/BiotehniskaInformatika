import numpy as np

def computeScore(iSeqA, iSeqB, iSubS, iSubM, iGapP):
    oScr = 0

    for A, B in zip(iSeqA, iSeqB):
        if A == '_' or B== '_':
            oScr += iGapP

        elif A != B:
            oScr += iSubM[iSubS.find(A), iSubS.find(B)]

        elif A == B:
            oScr += iSubM[iSubS.find(A), iSubS.find(B)] 

    return oScr