import matplotlib.pyplot as plt
import glob
from matplotlib import pyplot
import scipy.stats
import numpy as np
import random
import statistics as st


ti = 0
tf = 100.0
N = 2000
freq = 300.0


rand = []
for i in range(0, N):
    x = random.random()
    rand.append(x)


tiempo = np.linspace(ti, tf, N)
senal = 5* np.sin(2 * np.pi * freq * tiempo ) * rand
ps = np.abs(np.fft.fft(senal))**2
time_step = ((tf - ti)/N)

plt.figure(1)
plt.plot(tiempo,senal)

freqs = np.fft.fftfreq(senal.size, time_step)
idx = np.argsort(freqs)

plt.figure(2)
plt.plot(freqs[idx], ps[idx])
plt.show()

# asumiendo señal senoidal centrada en cero
SNR_dB = 20 * np.log10(max(senal)/max(rand)) 
print(SNR_dB)
SNR_dB_directo = 20 * np.log10(5/1) # como el seno tiene amplitud 5 y el rand va de 0 a 1 esta sería la formula teorica
print(SNR_dB - SNR_dB_directo)

# simulando el paquete signaltonoise asumiendo que calcula la media

media = st.mean(senal)
desvio = st.stdev(senal)

SNR_signaltonoise = media / desvio
print(SNR_signaltonoise)


plt.show()
