def computeRates(iTP, iTN, iFP, iFN):
    oTPR = iTP/(iTP + iFN)
    oTNR = iTN/(iTN + iFP)
    oFPR = iFP/(iTN + iFP)
    oFNR = iFN/(iTP + iFN)

    return(oTPR, oTNR, oFPR, oFNR)