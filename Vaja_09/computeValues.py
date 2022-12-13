def computeValues(iTP, iTN, iFP, iFN):
    oPPV = iTP/(iTP + iFP)
    oNPV = iTN/(iTN + iFN)
    oFDR = iFP/(iTP + iFP)
    oACC = (iTP + iTN)/(iTP + iTN + iFP + iFN)

    return oPPV, oNPV, oFDR, oACC