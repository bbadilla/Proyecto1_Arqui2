from multiprocesador import Core
import threading
import time 
import numpy as np
import random
from L1 import L1

class Chip(threading.Thread):
    number_chip = 0
    core0 = Core('',0,0,L1,L1)
    core1 = Core('',0,0,L1,L1)

    def __init__(self, number_chip, main_memory, cache1, cache2):
        self.number_chip = number_chip
        threading.Thread.__init__(self, name=number_chip, target=Chip.initCores, args=(self,number_chip,main_memory,cache1, cache2,))
        
    
    def initCores(self, number_chip, main_memory, cache1, cache2):
        #Invocacion de los Cores
        self.core0 = Core('P0',number_chip, main_memory, cache1, cache2)
        self.core1 = Core('P1',number_chip, main_memory, cache1, cache2)

        self.core0.start()
        self.core1.start()



        #core0_0.start()
        #core1_0.start()
        #core0_1.start()
        #core1_1.start()



