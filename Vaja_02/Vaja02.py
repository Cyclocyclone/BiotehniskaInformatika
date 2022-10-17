import numpy as np
import wfdb
import matplotlib.pyplot as plt
from detectWavepeaksQRS import detectWavePeaksQRS
from detectWavePeaksP import detectWavePeaks
from computeHB import computeHeartBeat
from detectWavePeaksT import detectWavePeaksT

# Load data
ecg = wfdb.rdrecord('e0104')
print(ecg.sig_name)
print(ecg.record_name)
print(ecg.units)
print(ecg.fs)

# parametri zajema
signal = 1
zac_cas = 0
nr_of_sec = 10

# izbira podatkov
ecg_s = np.array(ecg.p_signal)[zac_cas * ecg.fs : zac_cas * ecg.fs + ecg.fs * nr_of_sec]
ecg_s = ecg_s[:,signal]
ecg_t = np.arange(zac_cas, nr_of_sec, 1/ecg.fs)


# plot grafa
plt.figure()
plt.plot(ecg_t,ecg_s)
#plt.show()

iQ, iR, iS = detectWavePeaksQRS(ecg_s)
iP = detectWavePeaks(ecg_s, iQ, iS )
iT = detectWavePeaksT(ecg_s, iQ, iS)
plt.plot(ecg_t[iR], ecg_s[iR], 'o', color='green', linewidth=2, markersize=5)
plt.plot(ecg_t[iQ], ecg_s[iQ], 'o', color='red', linewidth=2, markersize=5)
plt.plot(ecg_t[iS], ecg_s[iS], 'o', color='blue', linewidth=2, markersize=5)
plt.plot(ecg_t[iP], ecg_s[iP], 'o', color='cyan', linewidth=2, markersize=5)
plt.plot(ecg_t[iT], ecg_s[iT], 'o', color='yellow', linewidth=2, markersize=5)
plt.title('EKG')
plt.xlabel('Čas [s]')
plt.ylabel('Vrednost')


QHBavg, QHBstd, QHFavg, QHFstd = computeHeartBeat(ecg_t[iQ], ecg_s[iQ])
print("Tocka Q - Povprecna perioda ", QHBavg, "s, stadardna deviacija: ", QHBstd, "s. Povprecna frekenca :", QHFavg, "Hz, standardna deviacija: ", QHFstd, "Hz.")

RHBavg, RHBstd, RHFavg, RHFstd = computeHeartBeat(ecg_t[iR], ecg_s[iR])
print("Tocka R - Povprecna perioda ", RHBavg, "s, stadardna deviacija: ", RHBstd, "s. Povprecna frekenca :", RHFavg, "Hz, standardna deviacija: ", RHFstd, "Hz.")

SHBavg, SHBstd, SHFavg, SHFstd = computeHeartBeat(ecg_t[iS], ecg_s[iS])
print("Tocka S - Povprecna perioda ", SHBavg, "s, stadardna deviacija: ", SHBstd, "s. Povprecna frekenca :", SHFavg, "Hz, standardna deviacija: ", SHFstd, "Hz.")

PHBavg, PHBstd, PHFavg, PHFstd = computeHeartBeat(ecg_t[iP], ecg_s[iP])
print("Tocka P - Povprecna perioda ", PHBavg, "s, stadardna deviacija: ", PHBstd, "s. Povprecna frekenca :", PHFavg, "Hz, standardna deviacija: ", PHFstd, "Hz.")




plt.show()