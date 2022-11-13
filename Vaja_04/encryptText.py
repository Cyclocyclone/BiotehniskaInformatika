from encodeBase64 import encodeBase64

def encryptText(iText, iKey):
    oText = ""

    for i in range (len(iText)):
        #znakl vhodnega besedila
        iChar = iText[i]
        iValue = ord(iChar)

        #znak ključa
        iKeyChar = iKey[i%len(iKey)]
        iKeyValue = ord(iKeyChar)

        #sestejemo
        oValue = iValue + iKeyValue
        oChar = chr(oValue)
        oText += oChar

    oText = encodeBase64(oText)

    return oText