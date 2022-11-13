from decodeBase64 import decodeBase64

def decryptText(iText, iKey):
    iText = decodeBase64(iText)
    oText = ''
    #print(iText)

    for i in range (len(iText)):
        #znakl vhodnega besedila
        iChar = iText[i]
        iValue = ord(iChar)

        #znak ključa
        iKeyChar = iKey[i%len(iKey)]
        iKeyValue = ord(iKeyChar)

        #sestejemo
        oValue = iValue - iKeyValue
        oChar = chr(oValue)
        oText += oChar
    return oText