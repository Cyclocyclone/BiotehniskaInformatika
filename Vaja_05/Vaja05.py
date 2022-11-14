import numpy as np
from solveModelSIR import solveModelSIR
from displayModel import displayModel

#stevilo prebivalcev
N = 7900000
I0 = 10

#-----------
#1 SIR, osnovni primer
t1 = 0
t2 = 150
dt = 1
beta = 1/2
gamma = 1/3

SIR, D = solveModelSIR([t1, t2, dt],[N-I0,I0,0],[beta, gamma])
displayModel(SIR)

