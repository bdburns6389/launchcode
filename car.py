class Car:
    
    def __init__(self, gas_level):
        self.gas_level = gas_level
    
    def add_gas(self, gas):
        self.gas_level = self.gas_level + gas
    
    def fill_up(self):
        if self.gas_level < 13:
            return 13 - self.gas_level
        else:
            return 0
            
car1 = Car(9)
print(car1.__dict__)

class Snowboard:
    
    def __init__(self, brand, model, length, camber):
        self.brand = brand
        self.model = model
        self.length = length
        self.camber = camber
        
    def __repr__(self):
        return "Board is: "+self.brand+" "+self.model+" "+str(self.length)+" "+self.camber
        
board1 = Snowboard("never_summer","proto",153,"hybrid")

def main():
    print (board1)
    
if __name__ == "__main__":
    main()