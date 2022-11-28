import numpy as np

def getPlanarProjection(iImage, iNormVec, iFun):
    oP = []

    Y, X, Z = np.shape(iImage)

    if iNormVec == [1, 0, 0]:
        oP = np.zeros([Y, Z])
        for z in range(Z):
            for y in range(Y):
                oP[y, z] = eval('np.' + iFun + '(iImage[y, :, z])')
    
    elif iNormVec == [0, 1, 0]:
        oP = eval('np.' + iFun + '(iImage, axis=0)')
    elif iNormVec == [0, 0, 1]:
        oP = eval('np.' + iFun + '(iImage, axis=2)')


    return oP
