
def  dict2xml(iDict, iXml, iOffset):
    oXml = iXml
    nl = '\n'
    f = iDict.keys()
    for key in f:
        if isinstance(iDict[key], dict):
            oXml = oXml + iOffset + '<' + key + '>' + nl
            oXml = dict2xml(iDict[key], oXml, iOffset + '   ') #4 presledki
            oXml = oXml + iOffset + '</' + key + '>' + nl
        else:
            oXml = oXml + iOffset + '<'+ key + '>' + str(iDict[key]) + '</' + key + '>' + nl
    return oXml 
