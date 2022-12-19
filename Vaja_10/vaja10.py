import numpy as np
import matplotlib.pyplot as plt

def bayesProbability(iPopRatio, iTestSens, iTestSpec):
    pBA = iTestSens/100 #TPR
    pA = iPopRatio/100 #delez populacije
    pBnA = 1-iTestSpec/100 #FPR = 1-TNR
    #Pogojna verjetnost v %
    oProb = pBA*pA/(pBA*pA+pBnA*(1-pA))*100
    return oProb


popRatio = 0.5
testSens = 99
testSpec = 99

P = bayesProbability(popRatio, testSens, testSpec)
print(P)

#naloga 2

testSens = np.linspace(0, 100, 101)
testSpec = testSens
P = bayesProbability(popRatio, testSens, testSpec)

plt.figure()
plt.plot(testSens, P)
plt.xlabel('TPR = TNR')
plt.ylabel('p(A|B)')
plt.show()

#naloga 3

popRatio = np.linspace(0, 100, 11)
plt.figure()
for i in range(len(popRatio)):
    P = bayesProbability(popRatio[i], testSens, testSpec)
    plt.plot(testSens, P)

plt.xlabel('TPR = TNR')
plt.ylabel('p(A|B)')
plt.legend(popRatio)
plt.show()