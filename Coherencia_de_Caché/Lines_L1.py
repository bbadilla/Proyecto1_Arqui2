
class Lines_L1:
    
    #Atributos
    state =  ' '
    data = ' '
    direction = ' '
    number = 0

    #Constructor
    def __init__(self, number, state, direction, data):
        self.number = number
        self.state = state
        self.direction = direction
        self.data = data

    def setLine(self, state, direction, data):
        self.state = state
        self.direction = direction
        self.data = data

    def getState(self):
        
