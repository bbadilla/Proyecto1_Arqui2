import threading
import time 
import numpy as np
import random
from memory import Memory
from L1 import L1
from threading import Thread, Lock
from control_L2 import Control_L2
import logging

class Control_L1(threading.Thread):

    bus = ' '


    def __init__(self):
        self


    def read(self, controlL2, direc_mem, cache_process00, cache_process01, cache_process10, cache_process11, cache_processL20, cache_processL21, memory, core, chip):

        logging.info('Busca el dato en la cache  L1 '+str(core)+','+str(chip))
        #Controlador de caches L1
        
        #Asignacion de caches a utilizar
        if (chip == 0):
            if (core == 'P0'):
                cache_request =  cache_process00
                cache_recive = cache_process01
            else:
                cache_request =  cache_process01
                cache_recive = cache_process00
        else:
            if (core == 'P0'):
                cache_request =  cache_process10
                cache_recive = cache_process11
            else:
                cache_request =  cache_process11
                cache_recive = cache_process10
                
        owner = ''
        line_change = direc_mem%2
        ##################################  Logica de Reads entre L1's  ############################
    

        #Acierta la posicion de memoria en cache
        if (cache_request.lines[line_change].direction == direc_mem):
            print('Estaba en cache')

            #Caso en el que la linea esta en invalido
            if (cache_request.lines[line_change].state == 'I'):
                #Mensaje en el bus
                bus = 'Read miss from cahe L1 '+str(cache_request.chip)+' '+str(cache_request.core)
                logging.info(bus)
                #Verifica los estados de la otra cache
                #Caso en que este M en la otra cache
                if (cache_recive.lines[line_change].state == 'M' and cache_recive.lines[line_change].direction == direc_mem):
                    cache_recive.lines[line_change].state = 'S'
                    owner = ','+cache_recive.core+','+str(cache_recive.chip)
                        
                #Llamada al control de L2 en caso invalido
                controlL2.read(direc_mem, cache_process00, cache_process01, cache_process10, cache_process11, cache_processL20, cache_processL21, chip, core, memory, owner)

            #Caso en el que la linea esta en Compartido o Modificado
            else:
                bus = 'Read Hit '+str(cache_request.chip)+' '+str(cache_request.core)
                logging.info(bus)
                return None
            
        #No Acierta la posicion de memoria en cache
        else:
            bus = 'Read miss from cahe L1 '+str(cache_request.chip)+' '+str(cache_request.core)
            logging.info(bus)
            #Verifica los estados de la otra cache
            if (cache_recive.lines[line_change].state == 'M' and cache_recive.lines[line_change].direction == direc_mem):
                cache_recive.lines[line_change].state = 'S'
                owner = ','+cache_recive.core+','+str(cache_recive.chip)
            controlL2.read(direc_mem, cache_process00, cache_process01, cache_process10, cache_process11, cache_processL20, cache_processL21, chip, core, memory, owner)
        print('')
        print ( str(cache_process00.chip)+'  '+str(cache_process00.core) +'  '+ str(cache_process00.lines[0].number) +'  '+ str(cache_process00.lines[0].state) +' '+ str(cache_process00.lines[0].directionBin)+ '  ' +str(cache_process00.lines[0].data))
        print ( str(cache_process00.chip)+'  '+str(cache_process00.core) +'  '+ str(cache_process00.lines[1].number) +'  '+ str(cache_process00.lines[1].state) +' '+ str(cache_process00.lines[1].directionBin)+ '  ' +str(cache_process00.lines[1].data))
        print('')
        print ( str(cache_process01.chip)+'  '+str(cache_process01.core) +'  '+ str(cache_process01.lines[0].number) +'  '+ str(cache_process01.lines[0].state) +' '+ str(cache_process01.lines[0].directionBin)+ '  ' +str(cache_process01.lines[0].data))
        print ( str(cache_process01.chip)+'  '+str(cache_process01.core) +'  '+ str(cache_process01.lines[1].number) +'  '+ str(cache_process01.lines[1].state) +' '+ str(cache_process01.lines[1].directionBin)+ '  ' +str(cache_process01.lines[1].data))
        print('')
        print ( str(cache_process10.chip)+'  '+str(cache_process10.core) +'  '+ str(cache_process10.lines[0].number) +'  '+ str(cache_process10.lines[0].state) +' '+ str(cache_process10.lines[0].directionBin)+ '  ' +str(cache_process10.lines[0].data))
        print ( str(cache_process10.chip)+'  '+str(cache_process10.core) +'  '+ str(cache_process10.lines[1].number) +'  '+ str(cache_process10.lines[1].state) +' '+ str(cache_process10.lines[1].directionBin)+ '  ' +str(cache_process10.lines[1].data))
        print('')
        print ( str(cache_process11.chip)+'  '+str(cache_process11.core) +'  '+ str(cache_process11.lines[0].number) +'  '+ str(cache_process11.lines[0].state) +' '+ str(cache_process11.lines[0].directionBin)+ '  ' +str(cache_process11.lines[0].data))
        print ( str(cache_process11.chip)+'  '+str(cache_process11.core) +'  '+ str(cache_process11.lines[1].number) +'  '+ str(cache_process11.lines[1].state) +' '+ str(cache_process11.lines[1].directionBin)+ '  ' +str(cache_process11.lines[1].data))
        print('')
        print ( str(cache_processL20.chip)+'  '+str(cache_processL20.lines[0].number) +'  '+ str(cache_processL20.lines[0].state) +' '+str(cache_processL20.lines[0].owner)+' '+str(cache_processL20.lines[0].directionBin)+ '  ' +str(cache_processL20.lines[0].data))
        print ( str(cache_processL20.chip)+'  '+str(cache_processL20.lines[1].number) +'  '+ str(cache_processL20.lines[1].state) +' '+str(cache_processL20.lines[1].owner)+' '+ str(cache_processL20.lines[1].directionBin)+ '  ' +str(cache_processL20.lines[1].data))
        print ( str(cache_processL20.chip)+'  '+str(cache_processL20.lines[2].number) +'  '+ str(cache_processL20.lines[2].state) +' '+str(cache_processL20.lines[2].owner)+' '+str(cache_processL20.lines[2].directionBin)+ '  ' +str(cache_processL20.lines[2].data))
        print ( str(cache_processL20.chip)+'  '+str(cache_processL20.lines[3].number) +'  '+ str(cache_processL20.lines[3].state) +' '+str(cache_processL20.lines[3].owner)+' '+ str(cache_processL20.lines[3].directionBin)+ '  ' +str(cache_processL20.lines[3].data))
        print('')
        print ( str(cache_processL21.chip)+'  '+str(cache_processL21.lines[0].number) +'  '+ str(cache_processL21.lines[0].state) +' '+str(cache_processL21.lines[0].owner)+' '+str(cache_processL21.lines[0].directionBin)+ '  ' +str(cache_processL21.lines[0].data))
        print ( str(cache_processL21.chip)+'  '+str(cache_processL21.lines[1].number) +'  '+ str(cache_processL21.lines[1].state) +' '+str(cache_processL21.lines[1].owner)+' '+ str(cache_processL21.lines[1].directionBin)+ '  ' +str(cache_processL21.lines[1].data))
        print ( str(cache_processL21.chip)+'  '+str(cache_processL21.lines[2].number) +'  '+ str(cache_processL21.lines[2].state) +' '+str(cache_processL21.lines[2].owner)+' '+str(cache_processL21.lines[2].directionBin)+ '  ' +str(cache_processL21.lines[2].data))
        print ( str(cache_processL21.chip)+'  '+str(cache_processL21.lines[3].number) +'  '+ str(cache_processL21.lines[3].state) +' '+str(cache_processL21.lines[3].owner)+' '+ str(cache_processL21.lines[3].directionBin)+ '  ' +str(cache_processL21.lines[3].data))
        print('')
        for x in range(16):
            print ('Memo principal ' +str(bin(memory.lines[x].position))+'  '+ str(memory.lines[x].state)+'  '+str(memory.lines[x].owner) +'  '+ str(memory.lines[x].data) )
        print(" ")


##########################Escribir en las L1

    def write(self, controlL2, direc_mem, cache_process00, cache_process01, cache_process10, cache_process11, cache_processL20, cache_processL21, memory, core, chip, data):
        logging.info('Peticion de escritura generada en la cache L1 '+str(core)+','+str(chip))
        #Asignacion de caches a utilizar
        if (chip == 0):
            if (core == 'P0'):
                cache_request =  cache_process00
                cache_recive = cache_process01
            else:
                cache_request =  cache_process01
                cache_recive = cache_process00
        else:
            if (core == 'P0'):
                cache_request =  cache_process10
                cache_recive = cache_process11
            else:
                cache_request =  cache_process11
                cache_recive = cache_process10
                
        owner = ''
        line_change = direc_mem%2

        #Escritura en caches y en memoria

        bus = 'Write Miss from cahe L1 '+str(cache_request.chip)+' '+str(cache_request.core)
        logging.info(bus)
        #Caso en que este M en la otra cache
        if ((cache_recive.lines[line_change].state == 'M' or cache_recive.lines[line_change].state == 'S') and cache_recive.lines[line_change].direction == direc_mem):
            cache_recive.lines[line_change].state = 'I'
            owner = ','+cache_recive.core+','+str(cache_recive.chip)
      
        controlL2.write(direc_mem, cache_process00, cache_process01, cache_process10, cache_process11, cache_processL20, cache_processL21, chip, core, memory, owner, data)

        print('')
        print ( str(cache_process00.chip)+'  '+str(cache_process00.core) +'  '+ str(cache_process00.lines[0].number) +'  '+ str(cache_process00.lines[0].state) +' '+ str(cache_process00.lines[0].directionBin)+ '  ' +str(cache_process00.lines[0].data))
        print ( str(cache_process00.chip)+'  '+str(cache_process00.core) +'  '+ str(cache_process00.lines[1].number) +'  '+ str(cache_process00.lines[1].state) +' '+ str(cache_process00.lines[1].directionBin)+ '  ' +str(cache_process00.lines[1].data))
        print('')
        print ( str(cache_process01.chip)+'  '+str(cache_process01.core) +'  '+ str(cache_process01.lines[0].number) +'  '+ str(cache_process01.lines[0].state) +' '+ str(cache_process01.lines[0].directionBin)+ '  ' +str(cache_process01.lines[0].data))
        print ( str(cache_process01.chip)+'  '+str(cache_process01.core) +'  '+ str(cache_process01.lines[1].number) +'  '+ str(cache_process01.lines[1].state) +' '+ str(cache_process01.lines[1].directionBin)+ '  ' +str(cache_process01.lines[1].data))
        print('')
        print ( str(cache_process10.chip)+'  '+str(cache_process10.core) +'  '+ str(cache_process10.lines[0].number) +'  '+ str(cache_process10.lines[0].state) +' '+ str(cache_process10.lines[0].directionBin)+ '  ' +str(cache_process10.lines[0].data))
        print ( str(cache_process10.chip)+'  '+str(cache_process10.core) +'  '+ str(cache_process10.lines[1].number) +'  '+ str(cache_process10.lines[1].state) +' '+ str(cache_process10.lines[1].directionBin)+ '  ' +str(cache_process10.lines[1].data))
        print('')
        print ( str(cache_process11.chip)+'  '+str(cache_process11.core) +'  '+ str(cache_process11.lines[0].number) +'  '+ str(cache_process11.lines[0].state) +' '+ str(cache_process11.lines[0].directionBin)+ '  ' +str(cache_process11.lines[0].data))
        print ( str(cache_process11.chip)+'  '+str(cache_process11.core) +'  '+ str(cache_process11.lines[1].number) +'  '+ str(cache_process11.lines[1].state) +' '+ str(cache_process11.lines[1].directionBin)+ '  ' +str(cache_process11.lines[1].data))
        print('')
        print ( str(cache_processL20.chip)+'  '+str(cache_processL20.lines[0].number) +'  '+ str(cache_processL20.lines[0].state) +' '+str(cache_processL20.lines[0].owner)+' '+str(cache_processL20.lines[0].directionBin)+ '  ' +str(cache_processL20.lines[0].data))
        print ( str(cache_processL20.chip)+'  '+str(cache_processL20.lines[1].number) +'  '+ str(cache_processL20.lines[1].state) +' '+str(cache_processL20.lines[1].owner)+' '+ str(cache_processL20.lines[1].directionBin)+ '  ' +str(cache_processL20.lines[1].data))
        print ( str(cache_processL20.chip)+'  '+str(cache_processL20.lines[2].number) +'  '+ str(cache_processL20.lines[2].state) +' '+str(cache_processL20.lines[2].owner)+' '+str(cache_processL20.lines[2].directionBin)+ '  ' +str(cache_processL20.lines[2].data))
        print ( str(cache_processL20.chip)+'  '+str(cache_processL20.lines[3].number) +'  '+ str(cache_processL20.lines[3].state) +' '+str(cache_processL20.lines[3].owner)+' '+ str(cache_processL20.lines[3].directionBin)+ '  ' +str(cache_processL20.lines[3].data))
        print('')
        print ( str(cache_processL21.chip)+'  '+str(cache_processL21.lines[0].number) +'  '+ str(cache_processL21.lines[0].state) +' '+str(cache_processL21.lines[0].owner)+' '+str(cache_processL21.lines[0].directionBin)+ '  ' +str(cache_processL21.lines[0].data))
        print ( str(cache_processL21.chip)+'  '+str(cache_processL21.lines[1].number) +'  '+ str(cache_processL21.lines[1].state) +' '+str(cache_processL21.lines[1].owner)+' '+ str(cache_processL21.lines[1].directionBin)+ '  ' +str(cache_processL21.lines[1].data))
        print ( str(cache_processL21.chip)+'  '+str(cache_processL21.lines[2].number) +'  '+ str(cache_processL21.lines[2].state) +' '+str(cache_processL21.lines[2].owner)+' '+str(cache_processL21.lines[2].directionBin)+ '  ' +str(cache_processL21.lines[2].data))
        print ( str(cache_processL21.chip)+'  '+str(cache_processL21.lines[3].number) +'  '+ str(cache_processL21.lines[3].state) +' '+str(cache_processL21.lines[3].owner)+' '+ str(cache_processL21.lines[3].directionBin)+ '  ' +str(cache_processL21.lines[3].data))
        print('')
        for x in range(16):
            print ('Memo principal ' +str(bin(memory.lines[x].position))+'  '+ str(memory.lines[x].state)+'  '+str(memory.lines[x].owner) +'  '+ str(memory.lines[x].data) )
        print(" ")
    


            