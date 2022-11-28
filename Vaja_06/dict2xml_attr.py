import numpy as np

def dict2xml_attr(iDict, iXML, iOffset):
    oXML = iXML
    nl = '\n'
    f = iDict.keys()

    for key in f:
        if isinstance(iDict[key], dict):
            oXML = oXML + iOffset + '<' + key + '>' + nl
            oXML = dict2xml_attr(iDict[key], oXML, iOffset + '   ')
            oXML = oXML + iOffset + '</' + key + '>' + nl

        else:
            oXML = oXML + iOffset + '<' + key

            if isinstance(iDict[key], int):
                oXML = oXML + ' type="number"'

            else:
                oXML = oXML + ' type="string"'
            
            oXML = oXML + '>' + str(iDict[key]) + '</' + key + '>' + nl

    return oXML