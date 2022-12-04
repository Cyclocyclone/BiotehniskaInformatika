import numpy as np
import math

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

    elif iNormVec[2] == 0:
        oP = np.zeros([X,Z])
        fi = math.atan(iNormVec[0]/iNormVec[1])

        for z in range(Z):
            toP = np.zeros([Y,X])
            
            for y in range(Y):
                for x in range(X):
                    x1 = x - X/2
                    y1 = y - Y/2
                    xt = round(math.cos(fi)*x1 - math.sin(fi)*y1 + X/2)
                    yt = round(math.sin(fi)*x1 + math.cos(fi)*y1 + X/2)

                    if((yt<Y) and (yt>0) and (xt<X) and (xt>0)):
                        toP[y,x] = iImage[yt, xt, z]
            
            for x in range(X):
                oP[x,z] = eval('np.' + iFun + '(toP[:, x])')

        oP = oP


    return oP
