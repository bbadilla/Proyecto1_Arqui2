import threading
import time 
import numpy as np
import random
from Lines_L2 import Lines_L2
import threading


class L2(threading.Thread):

    #Lineas de memoria caché
    chip = 0
    core = 'P0'
    line0 = Lines_L2(0,'',0,'0')
    line1 = Lines_L2(1,'',0,'0')
    line2 = Lines_L2(1,'',0,'0')
    line3 = Lines_L2(1,'',0,'0')
    
    lines = [line0, line1, line2, line3]

    def __init__(self, chip, core):
        self.chip = chip
        self.core = core

    def write(self, owner, direc, data, state):
        print('Esta es es la cache de '+str(self.core)+' Con el dato  '+str(data))

        for x in range (len(self.lines)):
            self.lines[x].setLine(state, owner, direc, data)

