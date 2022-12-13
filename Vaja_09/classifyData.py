import numpy as np

def classifyData(iTreshold, iTestData, iRefData):
    iTestData = iTestData.copy()
    iRefData = iRefData.copy()

    classData = (iTestData>iTreshold)*1
    oTP = np.sum(np.logical_and(classData, iRefData))
    oTN = np.sum(np.logical_and(np.abs(classData-1), np.abs(iRefData-1)))
    oFP = np.sum(np.logical_and(classData, np.abs(iRefData-1)))
    oFN = np.sum(np.logical_and(np.abs(classData-1), iRefData))

    return oTP, oTN, oFP, oFN