import csv
import numpy as np


dcmGroupsname = "dcmGroups.csv"
dcmGroups = np.loadtxt(dcmGroupsname, delimiter=";", dtype=str)


dcmElementsname = "dcmElements.csv"
dcmElements = np.loadtxt(dcmElementsname, delimiter=";", dtype=str)


def getDicomTagName(iTag):
    iTagG = iTag[:4]
    iGroupn = dcmGroups[:,0]
    for i in range(np.size(iGroupn)-1):
        if iTagG == iGroupn[i]:
            oGroupName = dcmGroups[i, 1]

    iElements = dcmElements[:,0]

    for n in range(np.size(iElements)-1):
        if iTag in iElements[n]:
            oElementName = dcmElements[n, 1]

    return oGroupName, oElementName 