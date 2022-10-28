from loadDicomFile import loadDicomFile
from getDicomDataElement import getDicomDataElement
from displayDicomImage import displayDicomImage

import numpy as np



#------------
path = 'image11.dcm'
dcmData = np.array(loadDicomFile(path))
#-----------
# image date

dcmImageDate = getDicomDataElement(dcmData, '0008,0023')
dcmImageStudyTime = getDicomDataElement(dcmData, '0008,0030')
dcmImagePatientName = getDicomDataElement(dcmData, '0010,0010')
dcmImageRows = getDicomDataElement(dcmData, '0028,0010')
dcmImageWindowWidth = getDicomDataElement(dcmData, '0028,1051')


print(dcmImageDate)
print(dcmImageStudyTime)
print(dcmImagePatientName)
print(dcmImageRows)
print(dcmImageWindowWidth)

displayDicomImage(dcmData,path)
