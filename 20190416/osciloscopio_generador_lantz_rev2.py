# -*- coding: utf-8 -*-
"""
@author: FLTambosco/Sabrinator/realmariano
2019
"""
from lantz import MessageBasedDriver
from lantz.core import Feat
from lantz.core import Action
import numpy as np
import time


class TekOsc(MessageBasedDriver):
    'driver osciloscopio TEK1002 instrumentacion y control basado en Lantz'
    
    version = '0.1'     #class version
    
    MANUFACTURER_ID = '0x0699'
    MODEL_CODE = '0x0363'
    
    @Feat(read_once=True)
    def idn(self):
        return self.query('*IDN?')
    
    @Feat()
    def parametros(self):
        return self.resource.query_ascii_values('WFMPRE:XZE?;XIN?;', separator=';' )
    
    @Feat()
    def timebase(self):
        return 1111  #dummy value para generar timebase de forma tal de poder utilizarlo luego en el setter.
    
    @timebase.setter
    def timebase(self, seconds):
        self.write('HOR:DEL:SCA {}'.format(seconds))
        
class TekGen(MessageBasedDriver):

    version = '0.1' 
    # tomado de https://github.com/agustin92/Instrumentacion.git

    MANUFACTURER_ID = '0x0699'
    MODEL_CODE = '0x0346'
    
    DEFAULTS = {'COMMON': {'write_termination': '\n','read_termination': '\n'}}
    
    @Feat()
    def identity(self):
        return self.query('*IDN?')
    
    @Feat()
    def amplitude(self):
        return float(self.query('SOUR1:VOLT:AMPL?'))
    
    @amplitude.setter
    def amplitude(self, volts, channel=1):
        self.write("SOUR{}:VOLT:AMPL {}".format(channel, volts))
        
    def frequency_set(self, hertz, channel=1):
        self.write("SOUR{}:FREQ:FIX {}".format(channel, hertz))
        
    def waveform_shape(self, shape = 'SIN', channel = 1):
        # Formas posibles: SIN, SQU, PULS, RAMP
        # PRNoise, DC|SINC|GAUSsian|LORentz|ERISe|EDECay|
        # HAVersine
        self.write('SOUR{}:FUNC:SHAPE {}'.format(channel, shape))
    
# =============================================================
# adicionado por hgrecco para poder mirar salida en la pantalla    
#import visa
#visa.log_to_screen()
# =============================================================


#(Osciloscopio,Generador)
#('USB0::0x0699::0x0363::C108011::INSTR', 'USB0::0x0699::0x0346::C034166::INSTR')

# ---------------------------------
# correr este codigo inicialmente para obtener direcciones tomadas por el osciloscopio y el generador

rm = visa.ResourceManager()
misinstrumentos= rm.list_resources()
print(misinstrumentos)


# ---------------------------------
# a partir de mis instrumentos obtenemos

with TekOsc.via_usb('C108011') as osci:
    print(osci.idn)
    print(osci.parametros)
    print(osci.idn)
    osci.timebase = 28
    t = osci.timebase
