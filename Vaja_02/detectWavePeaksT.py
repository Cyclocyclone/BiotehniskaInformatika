import numpy as np
#detekcija T valov
def detectWavePeaksT (iData, iIdxQ, iIdxS):
    oIdxT = iIdxQ[1:]

    for i in range(1, np.size(iIdxS)-1):
        od_kje = iIdxS[i] #začetek pri S
        do_kje = iIdxQ[i+1] # konec pri naslednjem Q
        for idx in range(od_kje, do_kje, 1):
            if iData[idx]>iData[oIdxT[i-1]]: #išči peak
                oIdxT[i-1]=idx

    oIdxT = oIdxT[:-1]


    return(oIdxT)