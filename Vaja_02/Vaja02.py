import numpy as np
import wfdb
import matplotlib.pyplot as plt
from detectWavepeaksQRS import detectWavePeaksQRS

# Load data
ecg = wfdb.rdrecord('e0104')
print(ecg.sig_name)
print(ecg.record_name)
print(ecg.units)
print(ecg.fs)

# parametri zajema
signal = 1
zac_cas = 0
nr_of_sec = 5

# izbira podatkov
ecg_s = np.array(ecg.p_signal)[zac_cas * ecg.fs : zac_cas * ecg.fs + ecg.fs * nr_of_sec]
ecg_s = ecg_s[:,signal]
ecg_t = np.arange(zac_cas, nr_of_sec, 1/ecg.fs)


# plot grafa
plt.figure()
plt.plot(ecg_t,ecg_s)
#plt.show()

iQ, iR, iS = detectWavePeaksQRS(ecg_s)
plt.plot(ecg_t[iR], ecg_s[iR], 'o', color='green', linewidth=2, markersize=5)
plt.plot(ecg_t[iQ], ecg_s[iQ], 'o', color='red', linewidth=2, markersize=5)
plt.plot(ecg_t[iS], ecg_s[iS], 'o', color='blue', linewidth=2, markersize=5)
plt.title('EKG')
plt.xlabel('Čas [s]')
plt.ylabel('Vrednost')

plt.show()