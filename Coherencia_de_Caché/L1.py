import threading
import time 
import numpy as np
import random
from Lines_L1 import Lines_L1
import threading


class L1(threading.Thread):

    #Lineas de memoria caché
    chip = 0
    core = 'P0'
    line0 = Lines_L1(0,'I',0,'0')
    line1 = Lines_L1(1,'I',0,'0')
    lines = [line0, line1]

    def __init__(self, chip, core):
        self.chip = chip
        self.core = core
        self.line0 = Lines_L1(0,'I',0,'0')
        self.line1 = Lines_L1(1,'I',0,'0')
        self.lines = [self.line0, self.line1]

    def write(self, n, direc, data, state):
        print('Esta es es la cache de '+str(self.core)+' Con el dato  '+str(data))
        if(n%2 == 0):
            self.line0.setLine(state, direc, data)
        else:
            self.line1.setLine(state, direc, data)

    def writeOnLine(self, line, direc, data, state):
        print('Esta es es la cache de '+str(self.core)+' Con el dato  '+str(data))
        line.setLine(state, direc, data)

        


    
