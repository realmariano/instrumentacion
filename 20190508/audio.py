# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:37:36 2019
@author: LuMiNi
"""

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import time


fsamp = 44100

def GeneradorArray(tau, frequency, Amplitude = 1, fs = 44100): #por default tiene 44100 y no hay que aclararsela
    if type(frequency) == int: #si el input de frecuencia es un dado valor, hace lo de siempre
        myarray = Amplitude*np.sin(np.linspace(0,tau,int(tau*fs))*frequency*(2*np.pi))
        return myarray
    Tiempos = np.linspace(0, tau, fs*tau)
    taufraccionado = tau/len(frequency) #fracciona en partes temporales iguales cada frecuencia
    
    i = 0
    myarray = np.linspace(0, 0, 0)
    Frecuencias = np.linspace(0, 0, 0)
    LastPoint = 0 #está para que el concatenado de todas las frecuencias sea correcto
    
    while i < len(frequency):
        PartialLinspace = np.linspace(0, taufraccionado, int(taufraccionado*fs))*frequency[i]*(2*np.pi) + LastPoint
        PartialArray = Amplitude*np.sin(PartialLinspace)
        PartialFrecuencias = np.linspace(frequency[i], frequency[i], len(PartialArray))
        myarray = np.concatenate((myarray, PartialArray))
        Frecuencias = np.concatenate((Frecuencias, PartialFrecuencias))
        i = i + 1
        LastPoint = PartialLinspace[-1]
    
    return myarray, Frecuencias, Tiempos
    
#Este pedazo de codigo calcula los tiempos que tarda numpy y pythonlists en armar el array.
#podemos ver que numpy tarda impresionantemente más tiempo (para 5 segundos de sweep tarda 90 segundos casi y python no llega a 1)
#
#def GeneradorArraySweepContinuo(tau, freqini, freqf, Amplitude = 1, fs = 44100): #por default tiene 44100 y no hay que aclararsela
#    frequency = np.linspace(freqini, freqf, fs*tau)
#    Tiempos = np.linspace(0, tau, fs*tau)
#    myarraylist = []
#    myarray = np.linspace(0, 0, 0)
#    i = 0
#    ti = time.time()
#    while i < len(frequency):
#        myarray = np.append(myarray, Amplitude*np.sin(Tiempos[i]*frequency[i]*2*np.pi))
#        i = i + 1
#    tf = time.time()
#    print('El np array tardó ', tf-ti)
#    ti = time.time()
#    i = 0
#    while i < len(frequency):
#        myarraylist.append(Amplitude*np.sin(Tiempos[i]*frequency[i]*2*np.pi))
#        i = i + 1
#    myarraylist = np.array(myarraylist)
#    tf = time.time()
#    print('El append de python tardó ', tf-ti)
#    return myarray, myarraylist, Tiempos

def GeneradorArraySweepContinuo(tau, freqini, freqf, Amplitude = 1, fs = 44100): #por default tiene 44100 y no hay que aclararsela
    frequency = np.linspace(freqini, freqf, fs*tau)
    Tiempos = np.linspace(0, tau, fs*tau)
    myarraylist = []
    i = 0
    while i < len(frequency):
        myarraylist.append(Amplitude*np.sin(Tiempos[i]*frequency[i]*2*np.pi))
        i = i + 1
    myarraylist = np.array(myarraylist)
    return myarraylist, frequency, Tiempos


#sd.play(funcion(3, fsamp, 440),fsamp)

#sd.stop()

#time.sleep(3)
#array = funcion(3, fsamp, 450)
#plt.plot(array)

def barrido():
    frecuencia = np.linspace(200, 600, 10)
    for f in frecuencia:
        myarray = GeneradorArray(1, fsamp, f)
        sd.play(myarray, fsamp)
        time.sleep(1)
        #print(f)
        
#barrido()
def pasaralista(a):
    b = list(a)
    c = []
    i = 0
    while i < len(b):
        c.append(float(b[i]))
        i = i + 1
    return c


def record(tau, fs):
    myrecording = sd.rec(int(tau*fs), samplerate=fs, channels=1, blocking=True)
    time_total = np.linspace(0, tau, int(tau*fs))
    return myrecording, time_total

myrecording, time_total = record(3, fsamp)

#print('my recording ', myrecording)
#print('time total', time_total)

#time.sleep(3)
#sd.wait()

plt.plot(pasaralista(myrecording))
#plt.plot(list(time_total), pasaralista(myrecording))

#plt.plot(myrecording)
#print(len(list(time_total)))
#print(len(list(pasaralista(myrecording))))
plt.show()



#%%
import matplotlib.pyplot as plt
arraynp, arraypy, Tiempo = GeneradorArraySweepContinuo(4, 100, 1000)

plt.plot(Tiempo, arraynp + 3, 'b', Tiempo, arraypy, 'r')
