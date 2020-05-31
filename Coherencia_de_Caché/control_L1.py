import threading
import time 
import numpy as np
import random
from memory import Memory
from L1 import L1
from threading import Thread, Lock


class Control_L1(threading.Thread):

    operation = ''
    direc_mem = 0
    bus = ' '
    state = 'I'


    def __init__(self, operation, direc_mem, memory):
        threading.Thread.__init__(self)
        self.operation = operation
        self.direc_mem = direc_mem



    def read(self, direc_mem, cache_process00, cache_process01, memory, core, chip):

        #Asignacion de caches a utilizar
        if (chip == 0):
            if (core == 'P0'):
                cache_request =  cache_process00
                cache_recive = cache_process01
                print('P0 procesa')
                print('Cache P0')
                print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[0].number) +'  '+ str(cache_request.lines[0].state) +' '+ str(cache_request.lines[0].directionBin)+ '  ' +str(cache_request.lines[0].data))
                print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[1].number) +'  '+ str(cache_request.lines[1].state) +' '+ str(cache_request.lines[1].directionBin)+ '  ' +str(cache_request.lines[1].data))
                print('Cache P1')
                print ( str(cache_recive.chip)+'  '+str(cache_recive.core) +'  '+ str(cache_recive.lines[0].number) +'  '+ str(cache_recive.lines[0].state) +' '+ str(cache_recive.lines[0].directionBin)+ '  ' +str(cache_recive.lines[0].data))
                print ( str(cache_recive.chip)+'  '+str(cache_recive.core) +'  '+ str(cache_recive.lines[1].number) +'  '+ str(cache_recive.lines[1].state) +' '+ str(cache_recive.lines[1].directionBin)+ '  ' +str(cache_recive.lines[1].data))

            else:
                print('P1 procesa')
                cache_request =  cache_process01
                cache_recive = cache_process00
                print('Cache P0')
                print ( str(cache_recive.chip)+'  '+str(cache_recive.core) +'  '+ str(cache_recive.lines[0].number) +'  '+ str(cache_recive.lines[0].state) +' '+ str(cache_recive.lines[0].directionBin)+ '  ' +str(cache_recive.lines[0].data))
                print ( str(cache_recive.chip)+'  '+str(cache_recive.core) +'  '+ str(cache_recive.lines[1].number) +'  '+ str(cache_recive.lines[1].state) +' '+ str(cache_recive.lines[1].directionBin)+ '  ' +str(cache_recive.lines[1].data))
                print('Cache P1')
                print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[0].number) +'  '+ str(cache_request.lines[0].state) +' '+ str(cache_request.lines[0].directionBin)+ '  ' +str(cache_request.lines[0].data))
                print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[1].number) +'  '+ str(cache_request.lines[1].state) +' '+ str(cache_request.lines[1].directionBin)+ '  ' +str(cache_request.lines[1].data))
               

        ##################################  Logica de Reads entre L1's  ############################
        #Casos por estados

        for i in range(2):
            print(" ")
            print('INICIO')

            #Acierta la posicion de memoria en cache
            if (cache_request.lines[i].direction == direc_mem):
                print("Esta en cache")

                #Caso en el que la linea esta en invalido
                if (cache_request.lines[i].state == 'I'):
                    print('Invalido')
                    print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[i].number) +'  '+ str(cache_request.lines[i].state) +' '+ str(cache_request.lines[i].directionBin)+ '  ' +str(cache_request.lines[i].data))
                    #Mensaje en el bus
                    bus = 'Read miss from cahe'+str(cache_request.chip)+' '+str(cache_request.core)
                    #Verifica los estados de la otra cache
                    for i in range(len(cache_recive.lines)):
                        #Caso en que este M en la otra cache
                        if (cache_recive.lines[i].state == 'M' and cache_recive.lines[i].direction == direc_mem):
                            cache_recive.lines[i].state = 'S'
                            print('Cache del procesador '+str(cache_recive.core))
                            print (str(cache_recive.chip)+'  '+str(cache_recive.core) +'  '+ str(cache_recive.lines[i].number) +'  '+ str(cache_recive.lines[i].state) +' '+ str(cache_recive.lines[i].directionBin)+ '  ' +str(cache_recive.lines[i].data))

                    #Busca en memoria
                    for x in range(16):
                        if (direc_mem == memory.lines[x].position):
                            cache_request.writeOnLine(cache_request.lines[i],  direc_mem, memory.lines[x].data, 'S')
                            print('Cache del procesador '+str(cache_request.core))
                            print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[i].number) +'  '+ str(cache_request.lines[i].state) +' '+ str(cache_request.lines[i].directionBin)+ '  ' +str(cache_request.lines[i].data))
                            time.sleep(6)
                            return None
                
                #Caso en el que la linea esta en Compartido o Modificado
                else:
                    print('Modificaco o Compartido')
                    print('Cache del procesador '+str(cache_request.core))
                    print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[i].number) +'  '+ str(cache_request.lines[i].state) +' '+ str(cache_request.lines[i].directionBin)+ '  ' +str(cache_request.lines[i].data))
                    return None
                
            #No Acierta la posicion de memoria en cache
            else:
                print('No estaba en cache')
                #Linea a cambiar
                line_change = memory%2
                #Caso en el que la linea esta en invalido

                #Caso en el que la linea esta en Compartido 
                if (cache_request.lines[line_change].state == 'S'):
                    print('Compartido')
                    print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[line_change].number) +'  '+ str(cache_request.lines[line_change].state) +' '+ str(cache_request.lines[line_change].directionBin)+ '  ' +str(cache_request.lines[line_change].data))
                    #Mensaje en el bus
                    bus = 'Read miss from cahe'+str(cache_request.chip)+' '+str(cache_request.core)
                    #Verifica los estados de la otra cache
                    for i in range(len(cache_recive.lines)):
                        #Caso en que este M en la otra cache
                        if (cache_recive.lines[line_change].state == 'M'):
                            if (cache_recive.lines[i].state == 'M' and cache_recive.lines[i].direction == direc_mem):
                                cache_recive.lines[i].state = 'S'
                                print('Cache del procesador '+str(cache_recive.core))
                                print (str(cache_recive.chip)+'  '+str(cache_recive.core) +'  '+ str(cache_recive.lines[i].number) +'  '+ str(cache_recive.lines[i].state) +' '+ str(cache_recive.lines[i].directionBin)+ '  ' +str(cache_recive.lines[i].data))

                        #Busca en memoria
                        for x in range(16):
                            if (direc_mem == memory.lines[x].position):
                                cache_request.writeOnLine(cache_request.lines[line_change],  direc_mem, memory.lines[x].data, 'S')
                                print('Cache del procesador '+str(cache_request.core))
                                print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[line_change].number) +'  '+ str(cache_request.lines[line_change].state) +' '+ str(cache_request.lines[line_change].directionBin)+ '  ' +str(cache_request.lines[line_change].data))
                                time.sleep(6)
                                return None

                elif (cache_request.lines[line_change].state == 'I'):
                    print('Invalido')
                    print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[line_change].number) +'  '+ str(cache_request.lines[line_change].state) +' '+ str(cache_request.lines[line_change].directionBin)+ '  ' +str(cache_request.lines[line_change].data))
                    #Mensaje en el bus
                    bus = 'Read miss from cahe'+str(cache_request.chip)+' '+str(cache_request.core)
                    #Verifica los estados de la otra cache
                    for i in range(len(cache_recive.lines)):
                        #Caso en que este M en la otra cache
                        if (cache_recive.lines[i].state == 'M' and cache_recive.lines[i].direction == direc_mem):
                            cache_recive.lines[i].state = 'S'
                            print('Cache del procesador '+str(cache_recive.core))
                            print (str(cache_recive.chip)+'  '+str(cache_recive.core) +'  '+ str(cache_recive.lines[i].number) +'  '+ str(cache_recive.lines[i].state) +' '+ str(cache_recive.lines[i].directionBin)+ '  ' +str(cache_recive.lines[i].data))

                    #Busca en memoria
                    for x in range(16):
                        if (direc_mem == memory.lines[x].position):
                            cache_request.writeOnLine(cache_request.lines[line_change],  direc_mem, memory.lines[x].data, 'S')
                            print('Cache del procesador '+str(cache_request.core))
                            print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[line_change].number) +'  '+ str(cache_request.lines[line_change].state) +' '+ str(cache_request.lines[line_change].directionBin)+ '  ' +str(cache_request.lines[line_change].data))
                            time.sleep(6)
                            return None
                    

                #Caso en el que la linea esta en Modificado
                else:
                    print('Modificado')
                    print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[line_change].number) +'  '+ str(cache_request.lines[line_change].state) +' '+ str(cache_request.lines[line_change].directionBin)+ '  ' +str(cache_request.lines[line_change].data))
                    #Mensaje en el bus
                    bus = 'Read miss from cahe'+str(cache_request.chip)+' '+str(cache_request.core)
                    #Verifica los estados de la otra cache
                    for i in range(len(cache_recive.lines)):
                        #Caso en que este M en la otra cache
                        if (cache_recive.lines[i].state == 'M' and cache_recive.lines[i].direction == direc_mem):
                            cache_recive.lines[i].state = 'S'
                            print('Cache del procesador '+str(cache_recive.core))
                            print (str(cache_recive.chip)+'  '+str(cache_recive.core) +'  '+ str(cache_recive.lines[i].number) +'  '+ str(cache_recive.lines[i].state) +' '+ str(cache_recive.lines[i].directionBin)+ '  ' +str(cache_recive.lines[i].data))

                        #Busca en memoria
                        for x in range(16):
                            if (direc_mem == memory.lines[x].position):
                                cache_request.writeOnLine(cache_request.lines[line_change],  direc_mem, memory.lines[x].data, 'S')
                                print('Cache del procesador '+str(cache_request.core))
                                print ( str(cache_request.chip)+'  '+str(cache_request.core) +'  '+ str(cache_request.lines[line_change].number) +'  '+ str(cache_request.lines[line_change].state) +' '+ str(cache_request.lines[line_change].directionBin)+ '  ' +str(cache_request.lines[line_change].data))
                                time.sleep(6)
                                return None
        
        for x in range(16):
            print ('Memo principal ' +str(bin(memory.lines[x].position))+'  '+ str(memory.lines[x].state)+'  '+str(memory.lines[x].owner) +'  '+ str(memory.lines[x].data) )
        print("ACABO")
        print(" ")
        cache_request = None
        cache_recive = None

    #########Escribir en las L1
    

    
    