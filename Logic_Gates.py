#Portas Lógicas

class LogicGate:
    def __init__(self, gate_name):
        self.name = gate_name
        self.output = None
        
    def getGatename(self):
        return self.name
    
    def getOutput(self):
        try:
            self.output = self.GateLogicPerform()
        except AttributeError:
            print('Você não pode usar "getOuput()" antes da chamada das classes inferiores\n')

        return self.output

#Portas binárias
class BinaryGates(LogicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return self.insertPinA() 
        else:
            return self.pinA
    
    def getPinB(self):
        if self.pinB is None:
            return self.insertPinB()
        else:      
            return self.pinB
    
    def insertPinA(self):
        while True:
            pinA_input = int(input(f'Digite a entrada do PINO "A" para a porta {self.getGatename()}: '))

            if pinA_input in (0, 1): #validando apenas binários
                return int(pinA_input) 
            else:
                print('Entrada Inválida')

    def insertPinB(self):
        while True:
            pinB_input = int(input(f'Digite a entrada do PINO "B" para a porta {self.getGatename()}: '))

            if pinB_input in (0, 1): 
                return int(pinB_input)
            else: 
                print('Entrada Inválida')

#Portas Unitáias
class UniGates(LogicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        self.pinA = None
    
    def getPinA(self):
        if self.pinA == None:
            return self.insertPinA()
        else:
            return self.pinA

    def insertPinA(self):
        while True:
            pinA_input = int(input(f'Digite a entrada do PINO "A" para a porta {self.getGatename()}: '))

            if pinA_input in (0, 1):
                return int(pinA_input)
            else:
                print('Entrada Inválida')

#PORTA AND
class AND(BinaryGates):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        
    def GateLogicPerform(self):
        print(f'Porta {self.__class__.__name__}')

        a = self.getPinA()
        if a not in [0, 1]:
            print('valor Inválido')
            a = self.getPinA()

        b = self.getPinB()
        if b not in [0, 1]:
            print('valor Inválido')
            b = self.getPinB()
        
        if a == 1 and b == 1:
            return 1
        else:
            return 0
#PORTA OR
class OR(BinaryGates):
    def __init__(self, gate_name):
        super().__init__(gate_name)

    def GateLogicPerform(self):
        print(f'Porta {self.__class__.__name__}')

        a = self.getPinA()
        if a not in [0, 1]:
            print('valor Inválido')
            a = self.getPinA()

        b = self.getPinB()
        if b not in [0, 1]:
            print('valor Inválido')
            b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1

#PORTA NOT
class NOT(BinaryGates):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        
    def GateLogicPerform(self):
        print(f'Porta {self.__class__.__name__}')

        a = self.getPinA()
        if a not in [0, 1]:
            print('valor Inválido')
            a = self.getPinA()

        if a == 0:
            return 1
        else:
            return 0