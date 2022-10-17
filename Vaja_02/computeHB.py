import numpy as np

def computeHeartBeat(iTime, iIdx):
    Times = []
    oHBavg = 0
    oHBstd = 0
    oHFavg = 0
    oHFstd = 0

    for i in range (0, (np.size(iTime) -1)):
        cas = iTime[i+1] - iTime[i]
        Times.append(cas)
        i += 1

    oHBavg = np.round(np.average(Times), 3)
    oHBstd = np.round(np.std(Times), 3)
    oHFavg = np.round(1/np.average(Times), 3)
    oHFstdvred = 1/np.array(Times)
    oHFstd = np.round(np.std(oHFstdvred), 3)
 
    return oHBavg, oHBstd, oHFavg, oHFstd   