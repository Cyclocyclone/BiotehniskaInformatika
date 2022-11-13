from decodeBase64 import decodeBase64

def decryptText(iText, iKey):
    iText = decodeBase64(iText)
    oText = ''


    for i in range (len(iText)):
        iChar = iText[i]
        iValue = ord(iChar)

        iKeyChar = iKey[i%len(iKey)]
        iKeyValue = ord(iKeyChar)

        oValue = iValue - iKeyValue
        oChar = chr(oValue)
        oText += oChar
    return oText