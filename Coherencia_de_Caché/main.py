import threading
import time 
import numpy as np
import random
from memory import Memory
from chip import Chip
from L1 import L1

def main():

    main_memory = Memory()
    cache_L1_00 = L1(0,'P0')
    cache_L1_01 = L1(0,'P1')
    cache_L1_10 = L1(1,'P0')
    cache_L1_11 = L1(1,'P1')

    #Invocacion para generar los chips
    chip0 = Chip(0, main_memory, cache_L1_00, cache_L1_01)
    #chip1 = Chip(1)
    chip0.start()
    #chip1.start()
    #Cahes
   
   


    #Definicion de la memoria principal


if __name__ == "__main__":
    main()
    