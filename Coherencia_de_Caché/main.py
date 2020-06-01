import threading
import time 
import numpy as np
import random
from memory import Memory
from chip import Chip
from L1 import L1
from L2 import L2
import logging

def main():

    main_memory = Memory()
    cache_L1_00 = L1(0,'P0')
    cache_L1_01 = L1(0,'P1')
    cache_L1_10 = L1(1,'P0')
    cache_L1_11 = L1(1,'P1')

    cache_L2_0 = L2(0)
    cache_L2_1 = L2(1)

    time.sleep(5)

    #Invocacion para generar los chips
    chip0 = Chip(0, main_memory, cache_L1_00, cache_L1_01, cache_L1_10, cache_L1_11, cache_L2_0, cache_L2_1)
    chip1 = Chip(1, main_memory, cache_L1_00, cache_L1_01, cache_L1_10, cache_L1_11, cache_L2_0, cache_L2_1)
    chip0.start()
    chip1.start()

   

    #Definicion de la memoria principal

if __name__ == "__main__":
    main()
    