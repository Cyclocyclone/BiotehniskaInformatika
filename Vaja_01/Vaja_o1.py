import numpy as np
from bubblesort import BubbleSort
from displayResults import displayResults

nVektor = np.random.randint(0, 100, 100)
displayResults(nVektor,'r','Urejene vrednosti')
print(nVektor)

Out=BubbleSort(nVektor)

print(Out)

displayResults(Out,'g','Urejene vrednosti')