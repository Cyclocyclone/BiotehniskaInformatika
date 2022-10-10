import matplotlib.pyplot as plt
import numpy as np
#Naredi plot rezultatov
def displayResults(iVektor,iColor,iName):
    location = np.linspace(0, np.size(iVektor)-1, np.size(iVektor))
    plt.plot(iVektor,location,'o',color=iColor,linewidth =2, markersize=12)
    plt.title=iName
    plt.xlabel=('Vrednost elementa')
    plt.ylabel=('Polzaj elementa')
    plt.grid
    plt.show()