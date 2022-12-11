import numpy as np
from computeMatrices import computeMatrices
from computeSequences import computeSequences


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