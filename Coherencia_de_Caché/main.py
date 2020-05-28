import threading
import time 
import numpy as np
import random
from multiprocesador import Core
from memory import Memory

def main():
    #Invocacion para generar los cores
    core0_0 = Core('P0',0,1)
    core1_0 = Core('P1',0,1)
    core0_1 = Core('P0',1,1)
    core1_1 = Core('P1',1,1)

    core0_0.start()
    core1_0.start()
    core0_1.start()
    core1_1.start()


if __name__ == "__main__":
    main()
    