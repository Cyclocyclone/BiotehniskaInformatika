import matplotlib.pyplot as plt
import numpy as np

def drawResults(iX, iY, iTitle, iLabelX, iLabelY):
    plt.figure()
    plt.plot(iX, iY, 'x-', linewidth = 2)
    plt.xlim([np.min(iX), np.max(iX)])
    plt.ylim([np.min(iY[~np.isnan(iY)]), np.max(iY[~np.isnan(iY)])])
    plt.title(iTitle)
    plt.xlabel(iLabelX)
    plt.ylabel(iLabelY)
    plt.show()