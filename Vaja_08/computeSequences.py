import numpy as np

def computeSequences(iSeqA, iSeqB, iTrcM):
    oSeqA = ''
    oSeqB = ''
    idxA, idxB, = np.shape(iTrcM)
    idxA -=1; idxB -=1

    while(idxA != 0 or idxB != 0):
        trc = str(iTrcM[idxA, idxB])

        if trc == 'D':
            oSeqA = iSeqA[idxA-1] + oSeqA
            oSeqB = iSeqB[idxB-1] + oSeqB
            idxA -=1; idxB -=1

        if trc == 'L':
            oSeqA = '_' + oSeqB
            oSeqB = iSeqB[idxB-1] + iSeqB
            idxB -=1

        if trc == 'U':
            oSeqA = iSeqA[idxA-1] + oSeqA
            oSeqB = '_' + oSeqB
            idxA -=1

    return oSeqA, oSeqB