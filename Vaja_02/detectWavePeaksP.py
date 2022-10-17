import numpy as np

def detectWavePeaks(iData, iTdxQ, iTdxS):
    oIdxP = iTdxQ[1:]

    for i in range(1, np.size(iTdxQ)):
        od_kje = iTdxQ[i]
        do_kje = int(iTdxQ[i]-np.ceil((iTdxQ[i]-iTdxS[i-1])/3))
        for idx in range(od_kje, do_kje, -1):
            if iData[idx]>iData[oIdxP[i-1]]:
                oIdxP[i-1]=idx

    return oIdxP