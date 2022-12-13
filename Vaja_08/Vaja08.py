import numpy as np
from computeMatrices import computeMatrices
from computeSequences import computeSequences
from computeScore import computeScore


seqA = 'GGATCGGAA'
seqB = 'GAATTCAGTA'

subS = 'AGCT'
subM = np.ones([4,4])*-1 + np.eye(4,4)*3

gapP = -2



##########################

scrM, trcM = computeMatrices(seqA, seqB, subS, subM, gapP)
print(scrM)
print(trcM)

seqA_opt, seqB_opt = computeSequences(seqA, seqB, trcM)
print(seqA_opt)
print(seqB_opt)

#naloga 1
ocena = computeScore(seqA_opt,seqB_opt, subS, subM, gapP)
print(ocena)

#naloga 2
print('naloga 2')
seqA = 'ACA'
seqB = 'CGACT'

subS = 'AGCT'
subM = np.ones([4,4])*-1 + np.eye(4,4)*3
gapP = -2

scrM, trcM = computeMatrices(seqA,seqB, subS, subM, gapP)
print(scrM)
print(trcM)

seqA_opt, seqB_opt = computeSequences(seqA, seqB, trcM)
print(seqA_opt)
print(seqB_opt)

ocena = computeScore(seqA_opt,seqB_opt, subS, subM, gapP)
print(ocena)

#naloga 3
print('naloga 3')
seqA = 'CTCTAGCATTAG'
seqB = 'GTGCACCCA'

subS = 'AGCT'
subM = np.ones([4,4])*-1 + np.eye(4,4)*3
gapP = -2

scrM, trcM = computeMatrices(seqA,seqB, subS, subM, gapP)
print(scrM)
print(trcM)

seqA_opt, seqB_opt = computeSequences(seqA, seqB, trcM)
print(seqA_opt)
print(seqB_opt)

ocena = computeScore(seqA_opt,seqB_opt, subS, subM, gapP)
print(ocena)

#naloga 4
print('naloga 4')
seqA = 'ACA'
seqB = 'CGACT'


subS = 'AGCT'
subM = np.ones([4,4])*-1 + np.eye(4,4)*3
x_index = [1,0,3,2]
y_index = [0,1,2,3]
subM[y_index,x_index] = 1

gapP = 0

scrM, trcM = computeMatrices(seqA,seqB, subS, subM, gapP)
print(scrM)
print(trcM)

seqA_opt, seqB_opt = computeSequences(seqA, seqB, trcM)
print(seqA_opt)
print(seqB_opt)

ocena = computeScore(seqA_opt,seqB_opt, subS, subM, gapP)
print(ocena)

#naloga 5
print('naloga 5')
seqA = 'CTCTAGCATTAG'
seqB = 'GTGCACCCA'


subS = 'AGCT'
subM = np.ones([4,4])*-1 + np.eye(4,4)*3
x_index = [1,0,3,2]
y_index = [0,1,2,3]
subM[y_index,x_index] = 1

gapP = 0

scrM, trcM = computeMatrices(seqA,seqB, subS, subM, gapP)
print(scrM)
print(trcM)

seqA_opt, seqB_opt = computeSequences(seqA, seqB, trcM)
print(seqA_opt)
print(seqB_opt)

ocena = computeScore(seqA_opt,seqB_opt, subS, subM, gapP)
print(ocena)