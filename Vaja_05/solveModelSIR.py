import numpy as np


def solveModelSIR(iTime, iModel, iParam):
    length_of_model = int(np.ceil(iTime[1]-iTime[0]/iTime[2]))
    oModel = np.zeros([length_of_model, 4])
    oModel[:,3] = np.linspace(iTime[0], iTime[1], length_of_model)
    oModel[0,0:3] = np.array(iModel)/sum(iModel)

    for n in range(length_of_model-1):
        oModel[n+1,0] = oModel[n,0] - iParam[0]*oModel[n,0]*oModel[n,1]*iTime[2]
        oModel[n+1,1] = oModel[n,1] + (iParam[0]*oModel[n,0]*oModel[n,1]-iParam[1]*oModel[n,1])*iTime[2]
        oModel[n+1,2] = oModel[n,2] + iParam[1]*oModel[n,1]*iTime[2]


    rep_stevilo = iParam[0]/iParam[1]
    maxN = np.argmax(oModel[:,1])
    return oModel, [rep_stevilo, maxN]