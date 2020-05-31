'''''
                self.bus = 'read miss en cache ' +str(cache_process.chip) +' '+str(cache_process.core)
                print ('Cache linea 0 ' + str(cache_process.chip)+'  '+str(cache_process.core) +'  '+ str(cache_process.line0.number) +'  '+ str(cache_process.line0.state) +' '+ str(cache_process.line0.direction)+ '  ' +str(cache_process.line0.data))
                print(self.bus)
                time.sleep(1)

        else:
            if (cache)
            for x in range(16):
                if (direc_mem == memory.lines[x].position):
                    cache_process.write(counter,  direc_mem, memory.lines[x].data, state)
                    time.sleep(6)
                    if (counter%2==0):
                        print ('Cache linea 0 ' + str(cache_process.chip)+'  '+str(cache_process.core) +'  '+ str(cache_process.line0.number) +'  '+ str(cache_process.line0.state) +' '+ str(cache_process.line0.direction)+ '  ' +str(cache_process.line0.data))
                    
                    else:
                        print ('Cache linea 1 ' + str(cache_process.chip)+'  '+str(cache_process.core) +'  '+ str(cache_process.line1.number) +'  '+ str(cache_process.line1.state) +' '+ str(cache_process.line1.direction)+ '  ' +str(cache_process.line1.data))
    '''''


    """"   def write(self, direc_mem, cache_process00, cache_process01, cache_process10, cache_process11, memory, counter, data, core, chip):
        state = 'M'
        print(' ')
        for x in range(16):
            if (direc_mem == memory.lines[x].position):
                cache_process.write(counter,  direc_mem, data, state)
                time.sleep(6)
                if (counter%2==0):
                    print ('Cache linea 0 ' + str(cache_process.chip)+'  '+str(cache_process.core) +'  '+ str(cache_process.line0.number) +'  '+ str(cache_process.line0.state) +' '+ str(cache_process.line0.direction)+ '  ' +str(cache_process.line0.data))
                
                else:
                    print ('Cache linea 1 ' + str(cache_process.chip)+'  '+str(cache_process.core) +'  '+ str(cache_process.line1.number) +'  '+ str(cache_process.line1.state) +' '+ str(cache_process.line1.direction)+ '  ' +str(cache_process.line1.data))
        
        memory.setLine(direc_mem, state, core, data)
        print(' ')
        for x in range(16):
            print ('Memo principal ' +str(bin(memory.lines[x].position))+'  '+ str(memory.lines[x].state)+'  '+str(memory.lines[x].owner) +'  '+ str(memory.lines[x].data) )""""