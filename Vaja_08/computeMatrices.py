import numpy as np

def computeMatrices(iSeqA, iSeqB, iSubS, iSubM, iGapP):
    lenA = len(iSeqA) + 1
    lenB = len(iSeqB) + 1

    oSrcM = np.array([[0]*lenB] * lenA)
    oTrcM = np.array([['']*lenB] * lenA)

    oTrcM[:,0] = 'U'
    oTrcM[0,:] = 'L'
    oTrcM[0,0] = 'X'
    options = ['D', 'L', 'U']

    for idxA in range(1, lenA):
        for idxB in range(1, lenB):
            i = iSubS.find(iSeqA[idxA-1])
            j = iSubS.find(iSeqB[idxB-1])

            oScrD = oSrcM[idxA-1, idxB-1] + iSubM[i,j]
            oScrL = oSrcM[idxA, idxB-1] + iGapP
            oScrU = oSrcM[idxA-1, idxB] + iGapP

            scrMax = np.max([oScrD, oScrL, oScrU])
            idxMax = np.argmax([oScrD, oScrL, oScrU])

            oSrcM[idxA, idxB] = scrMax
            oTrcM[idxA, idxB] = options[idxMax]

    return oSrcM, oTrcM