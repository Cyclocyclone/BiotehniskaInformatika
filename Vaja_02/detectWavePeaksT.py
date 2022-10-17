import numpy as np

def detectWavePeaksT (iData, iIdxQ, iIdxS):
    oIdxT = iIdxQ[1:]

    for i in range(1, np.size(iIdxS)-1):
        od_kje = iIdxS[i]
        do_kje = iIdxQ[i+1]
        for idx in range(od_kje, do_kje, 1):
            if iData[idx]>iData[oIdxT[i-1]]:
                oIdxT[i-1]=idx

    oIdxT = oIdxT[:-1]


    return(oIdxT)