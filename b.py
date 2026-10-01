class Phone:
    class_mfd = 2025
    num_phone = 0
    def __init__(self, model, ram, rom, price, color):
        
        self.model = model
        self.ram = ram
        self.rom = rom
        self.price = price 
        self.color = color
        Phone.num_phone += 1
        
    def pictures(self):
        #this is a method of our object i.e what the object can do
        print(f"{self.model} takes real good pictures")
    
    def gaming(self):
        print(f"{self.model} cannot handle large games")
        
    def describe(self):
        print(f"The brand new {self.model} has {self.ram} ram and {self.rom} rom available in {self.color} color and is priced at {self.price}")