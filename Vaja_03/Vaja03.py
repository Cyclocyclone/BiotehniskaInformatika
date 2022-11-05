from loadDicomFile import loadDicomFile
from getDicomDataElement import getDicomDataElement
from displayDicomImage import displayDicomImage

import numpy as np



#------------
path = 'image01.dcm'
dcmData = np.array(loadDicomFile(path))
#-----------
# image date

dcmImageDate = getDicomDataElement(dcmData, '0008,0023')
dcmImageTime = getDicomDataElement(dcmData, '0008,0033')
dcmImagePatientName = getDicomDataElement(dcmData, '0010,0010')
dcmImagePatientsAge = getDicomDataElement(dcmData, '0010,1010')
dcmImageRows = getDicomDataElement(dcmData, '0028,0010')
dcmImageWindowWidth = getDicomDataElement(dcmData, '0028,1051')

dcmImageStudyTime = getDicomDataElement(dcmData, '0008,0030')


print(dcmImageDate)
print(dcmImageTime)
print(dcmImagePatientName)
print(dcmImagePatientsAge)
print(dcmImageRows)
print(dcmImageWindowWidth)

print(dcmImageStudyTime)

displayDicomImage(dcmData,path)
