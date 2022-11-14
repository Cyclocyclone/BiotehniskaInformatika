import matplotlib.pyplot as plt
import numpy as np

def displayModel(iModel):
    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(iModel[:,3], iModel[:,0], color='blue', linewidth=2)
    ax1.plot(iModel[:,3], iModel[:,1], color='red', linewidth=2)
    ax1.plot(iModel[:,3], iModel[:,2], color='green', linewidth=2)

    ax1.legend(['st(t)', 'i(t)', 'r(t)'])
    ax1.grid()

    ax1.set(xlabel='time (days)', ylabel='delez populacije')

    ax2.stackplot(iModel[:,3], iModel[:,0], iModel[:,1], iModel[:,2], labels = ['st(t)', 'i(t)', 'r(t)'])
    ax2.set(xlabel='time (days)', ylabel='delez populacije')
    ax2.axis([np.min(iModel[:,3]),np.max(iModel[:,3]),0, 1])
    plt.show()
