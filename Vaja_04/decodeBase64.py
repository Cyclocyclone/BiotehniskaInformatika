from numpy import binary_repr
import numpy as np

def decodeBase64(iText):
    with open('tableBASE64and58.csv', 'r', encoding= 'utf-8-sig') as f:
        Base = [line.split(';') for line in f]
        base64 = np.array(Base)[:,0]
        #base58 = np.array(Base[:,1])
    
    binText = ''
    for i in range(len(iText)):
        iChar = iText[i]
        decValue = np.squeeze(np.where(base64 ==iChar))
        binValue = binary_repr(decValue, width=6)
        binText += binValue

    while np.mod(len(binText), 8):
        binText = binText[: -1]

    oText = ''
    for i in range(0, len(binText), 8):
        binValue = binText[i : i+8]
        decValue = int(binValue, 2)
        oChar = chr(decValue)
        oText += oChar
    return oText

