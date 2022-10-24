from getDicomDataElement import getDicomDataElement
import numpy as np
import matplotlib.pyplot as plt

def displayDicomImage(iData):

    # pridobi podatke
    dcmRows = getDicomDataElement(iData, '0028,0010')
    Y = dcmRows['value']
    dcmColumns = getDicomDataElement(iData, '0028,0011')
    X = dcmColumns['value']
    dcmBitsAllocated = getDicomDataElement(iData, '0028,0100')
    bAlloc = dcmBitsAllocated['value']
    dcmWindowCenter = getDicomDataElement(iData, '0028,1050')
    wCenter = np.array(dcmWindowCenter['value']).astype('int')
    dcmWindowWidth = getDicomDataElement(iData, '0028,1051')
    wWidth = np.array(dcmWindowWidth['value'][:-1]).astype('int') 
    rSlope = 1
    rIntercept = 0
    dcmModality = getDicomDataElement(iData, '0008,0060')
    if dcmModality['value'] == 'CT':
        dcmRescaleSlope = getDicomDataElement(iData, '0028,1053')
        rSlope = np.array(dcmRescaleSlope['value']).astype('int') 
        dcmRescaleIntercept = getDicomDataElement(iData, '0028,1052')
        rIntercept = np.array(dcmRescaleIntercept['value']).astype('int') 

    # pridobi sliko

    N = np.size(iData)
    iData = iData[int(N+1-X*Y*(bAlloc/8)):int(N)] 
    I = np.zeros([Y,X])
    for y in range(Y):
        for x in range(X):
            idx = ((y-1)*X+(x-1))*2+1
            I[y,x] = iData[idx+1]*(256**1) + iData[idx]*(256**0)

    # linearna preslikava
    rI = rSlope*I + rIntercept
    #linearno oknjenje
    wCenter = wCenter
    wI = rI
    idx = rI < (wCenter-wWidth/2)
    wI[idx] = 0
    idx = rI > wCenter+wWidth/2
    wI[idx] = 255
    #idx = find(rI >= wCenter-wWidth/2 & rI <= wCenter+wWidth/2);
    idx = (rI >= wCenter-wWidth/2) * (rI <= wCenter+wWidth/2)
    wI[idx] = (wI[idx] - (wCenter - wWidth/2))*255/wWidth;    
    # prikazi sliko
    plt.figure()
    plt.imshow(wI)
    plt.show()
    #figure('Name', 'DICOM slika', 'Color', [1 1 1]);
    #image(wI); colormap([1:255; 1:255; 1:255]'./255);
    #axis image;