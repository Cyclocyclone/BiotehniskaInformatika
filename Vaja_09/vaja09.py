import pickle
import numpy as np
from classifyData import classifyData
from computeRates import computeRates
from computeValues import computeValues
from drawResults import drawResults
from computeAUC import computeAUC

a_file = open('data.pkl', 'rb')
D = pickle.load(a_file)

tMin = 70
tMax = 170
tNum = 20

tValues= np.linspace(70,170,num = 20)
X, Y = np.shape(D['testData'])


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
for i in range(0, tNum):
    for j in range(0,4):
        TP[i,j], TN[i,j], FP[i,j], FN[i,j] = classifyData(tValues[i], D['testData'][:, j], D['refData'].T)
        TPR[i,j], TNR[i,j], FPR[i,j], FNR[i,j] = computeRates(TP[i,j], TN[i,j], FP[i,j], FN[i,j])
        PPV[i,j], NPV[i,j], FDR[i,j], ACC[i,j] = computeValues(TP[i,j], TN[i,j], FP[i,j], FN[i,j])
        print(j)
        

""" print(TP)
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
print(ACC)  """

#Naloga 1
drawResults(tValues, TPR, 'TPR Nal1', 'Prag t', 'TPR')
drawResults(tValues, TNR, 'TNR Nal1', 'Prag t', 'TNR')
drawResults(tValues, FPR, 'FPR Nal1', 'Prag t', 'FPR')
drawResults(tValues, FNR, 'FNR Nal1', 'Prag t', 'FNR')
##############################
#Naloga 2
drawResults(tValues, PPV, 'PPV Nal2', 'Prag t', 'PPV')
drawResults(tValues, NPV, 'NPV Nal2', 'Prag t', 'NPV')
drawResults(tValues, FDR, 'FDR Nal2', 'Prag t', 'FDR')
drawResults(tValues, ACC, 'ACC Nal2', 'Prag t', 'ACC')
#############################
#Naloga 4
S = np.zeros(Y)
for k in range(Y):
    S[k] = computeAUC(FPR[:,k], TPR[:,k])
print('Povrsina pod ROC', S)

drawResults(TPR, TNR, 'ROC Krivulja', 'False positive rate', 'True positive rate')
#############################
#Naloga 5
ACC_Max = np.argmax(ACC, axis=0)
optiT = tValues[ACC_Max]
print('Maksimalni ACC:', ACC_Max, '. Optimalni prag t:', optiT)
############################
#Naloga 7
tValue_7 = 120
TP, TN, FP, FN = classifyData(tValue_7, D['testData'][:,0], D['refData'].T)
#TABELA 1
Tabela1 = np.empty([4,4], dtype=object)
#1 vrstica
Tabela1[0,0] = ''
Tabela1[0,1] = 'Pozitivni'
Tabela1[0,2] = 'Negativni'
Tabela1[0,3] = 'Skupaj'
#2 vrstica
Tabela1[1,0] = 'Pravilno'
Tabela1[1,1] = str(TP)
Tabela1[1,2] = str(TN)
Tabela1[1,3] = str(TN+FP)
#3 vrstica
Tabela1[2,0] = 'Nepravilno'
Tabela1[2,1] = str(FP)
Tabela1[2,2] = str(FN)
Tabela1[2,3] = str(FP+FN)
#4 vrstica
Tabela1[3,0] = 'Skupaj'
Tabela1[3,1] = str(TP+FP)
Tabela1[3,2] = str(TN+FN)
Tabela1[3,3] = str(TN+TP+FP+FN)

print(Tabela1)
##################################
#Tabela 2
Tabela2 = np.empty([9, 5], dtype=object)
#1 vrstica
Tabela2[0,0] = 'Vrednost'
Tabela2[0,1] = 'Test 1'
Tabela2[0,2] = 'Test 2'
Tabela2[0,3] = 'Test 3'
Tabela2[0,4] = 'Test 4'

#1 Stolpec
Tabela2[1,0] = 'TPR'
Tabela2[2,0] = 'TNR'
Tabela2[3,0] = 'FPR'
Tabela2[4,0] = 'FNR'
Tabela2[5,0] = 'PPV'
Tabela2[6,0] = 'NPV'
Tabela2[7,0] = 'FDR'
Tabela2[8,0] = 'ACC'

for t in range (4):
    TP, TN, FP, FN = classifyData(tValue_7, D['testData'][:,t], D['refData'].T)
    TPR, TNR, FPR, FNR = computeRates(TP, TN, FP, FN)
    PPV, NPV, FDR, ACC = computeValues(TP, TN, FP, FN)
    i = t+1
    Tabela2[1,i] = TPR
    Tabela2[2,i] = TNR
    Tabela2[3,i] = FPR
    Tabela2[4,i] = FNR
    Tabela2[5,i] = PPV
    Tabela2[6,i] = NPV
    Tabela2[7,i] = FDR
    Tabela2[8,i] = ACC



print(Tabela2)