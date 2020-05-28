import threading
import time 
import numpy as np
import random


#Clase core
class Core(threading.Thread):

    #Atributos no definidos
    operation = ''
    memory = ''
    data = ''
    core = ''
    chip = 0

    #Constructor
    def __init__(self, core, chip, t):
        threading.Thread.__init__(self, name=core, target=Core.instruction_generator, args=(self,t,))
        self.core = core
        self.chip = chip

    def instruction_generator(self, t):

        #Distribucion binomial para las instrucciones
        distribution = np.random.binomial(10,0.5,1000)%3

        #Distribucion binomial para la direcciones de memoria
        memory = np.random.binomial(25,0.5,1000)%16
        #print(memory)
        data_write = ''

        #Generador de instrucciones
        for i in range(len(distribution)):

            #Instruccion de lectura
            if(distribution[i]==0):
                self.operation = 'READ'
                self.memory = bin(memory[i])
                print(self.core + ','+str(self.chip)+': '+self.operation+' '+str(self.memory))

            #Instruccion de escritura
            elif(distribution[i]==2):
                for x in range(4):
                    data_write += random.choice('ABCDEFG123456789')
                self.operation = 'WRITE'
                self.memory = bin(memory[i])
                self.data = data_write
                data_write = ''
                print(self.core + ','+str(self.chip)+': '+self.operation+' '+str(self.memory)+'; '+self.data)

            #Instruccion de CALC
            else:
                self.operation = 'CALC'
                print(self.core + ','+str(self.chip)+': '+self.operation)
        #print(self.core + ','+str(self.chip))
            time.sleep(t)

