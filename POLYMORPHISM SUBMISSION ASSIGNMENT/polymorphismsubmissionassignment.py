#Create a parent class
class ComputerPart():
    #properties for child classes to inherit
    name = "Unknown"
    price = None
    availabilty = True

    #get info method returns a string describing the part
    def getInfo(self):
        msg = "{} has a price of {}. Is the part available: {}".format(self.name, self.price, self.availabilty)
        return msg

    

#Child class
class GraphicsCard(ComputerPart):
    #inheriting parent attributes but also changing them to fit child
    name = "GTX 4090"
    price = 2500
    vram = "8GB"
    clock_speed = "2.1MHz"
    availability = False

    #utilizing polymorphism on parent class method
    def getInfo(self):
        msg = "{0} has a price of {1}. Is the part available: {2}\nThe {0} has {3} of VRAM and a clock speed of {4}".format(self.name, self.price, self.availabilty, self.vram, self.clock_speed)
        return msg





#Another child class
class CPU(ComputerPart):
    #inheriting parent attributes but also changing them to fit child
    name = "AMD 5900X"
    price = 400
    supported_ram = "128GB"

    #utilizing polymorphism on parent class method
    def getInfo(self):
        msg = "{} has a price of {}. Is the part available: {}\nIt supports {} of ram".format(self.name, self.price, self.availabilty, self.supported_ram)
        return msg



if __name__ == "__main__":

#printing out info to console using methods from both child classes
    gpu = GraphicsCard()
    print(gpu.getInfo())

    cpu = CPU()
    print(cpu.getInfo())
    
