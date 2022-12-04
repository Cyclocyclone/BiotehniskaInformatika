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

print('neki')

xc = 60
#sagCS = getPlanarCrossSection(img, [0, 0, 1], xc)
#displayImage(sagCS, 'xc = 60')

yc = 35
#sagCS = getPlanarCrossSection(img, [1, 0, 0], yc)
#displayImage(sagCS, 'yc = 35')

zc = 90
#sagCS = getPlanarCrossSection(img, [0, 1, 0], zc)
#displayImage(sagCS, 'zc = 90')
#--------

#fun = 'max'
#sagP = getPlanarProjection(img, [1, 1, 0], fun)
#displayImage(sagP, '[9.24, 3.83, 0]')

#sagP = getPlanarProjection(img, [0, 1, 0], fun)
#displayImage(sagP, '010 max')

#sagP = getPlanarProjection(img, [1, 0, 0], fun)
#displayImage(sagP, '100 max')

#sagP = getPlanarProjection(img, [0, 0, 1], fun)
#displayImage(sagP, '001 max')

#fun = 'mean'

#sagP = getPlanarProjection(img, [0, 1, 0], fun)
#displayImage(sagP, '010 mean')

#sagP = getPlanarProjection(img, [1, 0, 0], fun)
#displayImage(sagP, '100 mean')

#sagP = getPlanarProjection(img, [0, 0, 1], fun)
#displayImage(sagP, '001 mean')


fun = 'max'

sagP = getPlanarProjection(img, [3.83, 9.24, 0], fun)
print('neki2')
displayImage(sagP, '[3.83, 9.24, 0] max')

sagP = getPlanarProjection(img, [1, 1, 0], fun)
displayImage(sagP, '[1, 1, 0] max')

sagP = getPlanarProjection(img, [9.24, 3.83, 0], fun)
displayImage(sagP, '[9.24, 3.83, 0] max')
