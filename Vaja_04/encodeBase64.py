import base64

from numpy import binary_repr
import numpy as np

def encodeBase64(iText):
    with open('tableBASE64and58.csv', 'r', encoding= 'utf-8-sig') as f:
        Base = [line.split(';') for line in f]
        base64 = np.array(Base)[:,0]
        #base58 = np.array(Base[:,1])

    binText = ''

    for i in range(len(iText)):
        decValue = ord(iText[i]) 
        binValue = binary_repr(decValue, width=8)
        binText += binValue

    while np.mod(len(binText), 6):
        binText += '0'

    oText = ''
    for i in range(0, len(binText), 6):
        binValue = binText[i: i+6]
        decValue = int(binValue, 2)
        oChar = base64[decValue]
        oText += oChar
    return oText



