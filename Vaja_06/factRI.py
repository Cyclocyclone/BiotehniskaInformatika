import numpy as np

def factI (iValue):
 return np.math.factorial(iValue)

def factR (iValue):
    if iValue <= 0:
        return 0
    elif iValue == 1:
        return 1
    else:
        return iValue * factR(iValue - 1)
