import numpy as np
import matplotlib.pyplot as pltpy
import matplotlib as plt

aux = np.arange(0, 2*np.pi, 0.1)  #start,stop,step
y = np.cos(aux)

pltpy.plot(aux,y)
pltpy.show()
 