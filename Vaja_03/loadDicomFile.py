import numpy as np

def loadDicomFile(iPath):
    text = np.fromfile(iPath, dtype='uint8')
    return text