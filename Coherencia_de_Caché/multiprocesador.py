import threading
from threading import Thread, Lock
import time 
import numpy as np
import random
from L1 import L1
import queue
from control_L1 import Control_L1

mutex = Lock()

#Clase core
class Core(threading.Thread):

    #Atributos no definidos
    operation = ''
    memory = ''
    data = ''
    core = ''
    chip = 0


    #Constructor
    def __init__(self, core, chip, main_memory, cache1, cache2):
        threading.Thread.__init__(self, name=core, target=Core.instruction_generator, args=(self, main_memory,cache1, cache2, core, chip,))
        self.core = core
        self.chip = chip


        
    def instruction_generator(self, main_memory,cache1,cache2,core, chip):
        
        #Contador
        counter = 0
        #print(memory)
        data_write = ''

        control = Control_L1()

        #Generador de instrucciones
        while True:
        
            #Distribucion binomial para las instrucciones
            distribution = np.random.binomial(10,0.5)%3

            #Distribucion binomial para la direcciones de memoria
            memory = np.random.binomial(25,0.5)%16
            aux_memory = memory

            mutex.acquire()
            #mutex.acquire()
            #Instruccion de lectura
            if(distribution==0):
                self.operation = 'READ'
                self.memory = bin(memory)
                print(self.core + ','+str(self.chip)+': '+self.operation+' '+str(self.memory))     
                control.read(aux_memory, cache1,cache2,  main_memory, self.core, self.chip)
                #print (str(self.cache_L1.chip)+'  '+str(self.cache_L1.core) +'  '+ str(self.cache_L1.line0.number) +'  '+ str(self.cache_L1.line0.state) +' '+ str(self.cache_L1.line0.direction)+ '  ' +str(self.cache_L1.line0.data))
                time.sleep(5)    
                counter += 1    
                print(' ')

   

            #Instruccion de escritura
            elif(distribution==2):
                for x in range(4):
                    data_write += random.choice('ABCDEF123456789')
                self.operation = 'WRITE'
                self.memory = bin(memory)
                self.data = data_write
                print(self.core + ','+str(self.chip)+': '+self.operation+' '+str(self.memory)+'; '+self.data)
                control.write(aux_memory, cache1, cache2, main_memory,  self.core, self.chip, self.data)
                data_write = ''
                #time.sleep(10)    
                #counter += 1 
                print(' ')



            #Instruccion de CALC
            else:
                self.operation = 'CALC'
                print(self.core + ','+str(self.chip)+': '+self.operation)
                print(' ')

            mutex.release()


        #print(self.core + ','+str(self.chip))
            time.sleep(1)
            



