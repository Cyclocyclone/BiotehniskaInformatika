import pickle
import numpy as np
from classifyData import classifyData
from computeRates import computeRates
from computeValues import computeValues
from drawResults import drawResults

a_file = open('data.pkl', 'rb')
D = pickle.load(a_file)

tMin = 70
tMax = 170
tNum = 20

tValues= np.linspace(70,170,num = 20)

TP = np.zeros((20, 4))
TN = np.zeros((20, 4))
FP = np.zeros((20, 4))
FN = np.zeros((20, 4))

TPR = np.zeros((20, 4))
TNR = np.zeros((20, 4))
FPR = np.zeros((20, 4))
FNR = np.zeros((20, 4))

PPV = np.zeros((20, 4))
NPV = np.zeros((20, 4))
FDR = np.zeros((20, 4))
ACC = np.zeros((20, 4))
for i in range(0, tNum-1):
    for j in range(0,4):
        TP[i,j], TN[i,j], FP[i,j], FN[i,j] = classifyData(tValues[i], D['testData'][:, j], D['refData'].T)
        TPR[i,j], TNR[i,j], FPR[i,j], FNR[i,j] = computeRates(TP[i,j], TN[i,j], FP[i,j], FN[i,j])
        PPV[i,j], NPV[i,j], FDR[i,j], ACC[i,j] = computeValues(TP[i,j], TN[i,j], FP[i,j], FN[i,j])
        print(j)
        
drawResults(TPR, TNR, 'a', 'a', 'a')
print(TP)
print(TN)
print(FP)
print(FN)
print('---------')

print(TPR)
print(TNR)
print(FPR)
print(FNR)
print('-------------')


print(PPV)
print(NPV)
print(FDR)
print(ACC)


