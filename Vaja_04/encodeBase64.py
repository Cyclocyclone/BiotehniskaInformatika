import base64

from numpy import binary_repr
import numpy as np

def encodeBase64(iText):
    with open('C:/Users/cs5857/Vaje_bi_CS/Vaja_4/tableBASE64and58.csv', 'r', encoding= 'utf-8-sig') as f:
        Base = [line.split(';') for line in f]
        base64 = np.array(Base)[:,0]
        #base58 = np.array(Base[:,1])

    binText = ''
    #for Char in iText:
        #decValue = ord(Char)
    for i in range(len(iText)):
        decValue = ord(iText[i]) #decimalno
        binValue = binary_repr(decValue, width=8) #binarno
        binText += binValue

    #dodamo zakljucne bite
    while np.mod(len(binText), 6):
        binText += '0'

    #pretvori binarno besedilo v base64, pogleda kje je, ga doda in ga izpise vn
    oText = ''
    for i in range(0, len(binText), 6):
        binValue = binText[i: i+6]
        decValue = int(binValue, 2) #bin2dec int
        oChar = base64[decValue]
        oText += oChar
    return oText



