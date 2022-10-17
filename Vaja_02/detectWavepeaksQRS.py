import numpy as np

def detectWavePeaksQRS(iData):
    oIdxQ = []
    oIdxR = []
    oIdxS = []

    # Prag 80% razpona
    tData = min(iData) + 0.8 * (max(iData)-min(iData))

    idx = 0
    
    while idx<np.size(iData):
        if iData[idx] > tData:
            #index R
            idxR = idx
            while iData[idxR+1] > iData[idxR]:
                idxR = idxR + 1
            #dodaj h staremu
            oIdxR.append(idxR)

            #Index Q
            idxQ = idxR-1
            while iData[idxQ-1] <= iData[idxQ]:
                idxQ = idxQ -1
            oIdxQ.append(idxQ)

            #Index S    
            idxS = idxR+1
            while iData[idxS+1] <= iData[idxS]:
                idxS = idxS + 1
            oIdxS.append(idxS)

            idx = idxS

            
        
        idx += 1



    return oIdxQ, oIdxR, oIdxS