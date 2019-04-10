# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:34:30 2019

@author: Publico
"""
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt


#aux = np.arange(0,np.pi,0.1) # inicio, final, paso
#y=np.cos(aux)
#
#plt.plot(aux,y)
#plt.show()


def cos (I,F,P,A,W):
    aux = np.arange(I,F,P) # inicio, final, paso
    y=A*np.cos(W*aux)
    
    plt.plot(aux,y)
    plt.show()
    return
    
for x in range(1,4, 1):
    cos(0,12,0.1,x*0.5,2.0)
    
    
#for x in range(1,4, 1):
#    aux = np.arange(I,F,P)
#    y=A*np.cos(W*aux)
#    
#    plt.plot(aux,y)
#    plt.show()