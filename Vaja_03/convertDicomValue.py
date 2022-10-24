import numpy as np


def convertDicomValue(iValue, iVR):
    oValue = ''

    if iVR in ['AS','CS', 'DA', 'DS', 'LO', 'PN', 'SH', 'ST', 'TM']:
        for i in iValue:
            oValue += chr(i)

    elif iVR == 'UL':
        oValue = iValue[0]*(256**0)+iValue[1]*(256**1)+iValue[2]*(256**2)+iValue[3]*(256**3)
    elif iVR == 'US':
        oValue = iValue[0]*(256**0)+iValue[1]*(256**1)
    return oValue