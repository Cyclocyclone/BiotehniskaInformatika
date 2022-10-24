import numpy as np
from convertDicomValue import convertDicomValue
from getDicomTagName import getDicomTagName

def getDicomDataElement (iData, iTag):

    for i in range(np.size(iData)-8):
        s = iData[i+0] * (256**0) + iData[i+1]*(256**1)
        ssss = hex(s).lstrip("0x")
        ssss = ssss.zfill(4)

        e = iData[i+2] * (256**0) + iData[i+3]*(256**1)
        eeee = hex(e).lstrip("0x")
        eeee = eeee.zfill(4)
        tag = str(ssss) + ',' + str(eeee)

        if tag == iTag:
            print("Stop")
            break

    oElement = {}  
    oElement['idx'] = i
    oElement['teg'] = tag
    oElement['VR'] = chr(iData[i+4]) + chr(iData[i+5])
    oElement['VL'] = iData[i+6]*(256**0)+iData[i+7]*(256**1)
    oElement['value'] = iData[i+8:i+8+oElement['VL']]
    oElement['value'] = convertDicomValue(oElement['value'], oElement['VR'])
    oElement['group'], oElement['element'] = getDicomDataElement(iTag)


    return oElement