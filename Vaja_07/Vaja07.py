import nibabel as nib
import numpy as np
from getPlanarCrossSection import getPlanarCrossSection
import matplotlib.pyplot as plt
from getPlanarProjection import getPlanarProjection

def displayImage(iImage,iName = 'GeneralName'):
    plt.figure()
    plt.imshow(iImage, cmap=plt.cm.gray)
    plt.title(iName)
    plt.show()

img = nib.load("lung_001.nii.gz")
img = np.array(img.dataobj)
img = np.flip(img)
img = np.transpose(img, [2, 1, 0])

xc = 256
sagCS = getPlanarCrossSection(img, [1, 0, 0], xc)
#displayImage(sagCS)

#--------

fun = 'mean'
sagP = getPlanarProjection(img, [0, 0, 1], fun)
displayImage(sagP)


