import matplotlib.pyplot as plt
import numpy as np

def drawResults(iX, iY, iTitle, iLabelX, iLabelY):
    plt.figure()
    plt.plot(iX, iY, 'x-', linewidth = 2)
    plt.xlim([np.max(iX), np.min(iX)])
    plt.ylim([np.min(iY[~np.isnan(iY)]), np.max(iY[~np.isnan(iY)])])
    plt.title(iTitle)
    plt.xlabel(iLabelX)
    plt.ylabel(iLabelY)
    plt.savefig(iTitle, dpi=150)
    #plt.show()
    print(iTitle, 'Shranjeno')
