class Engine:
    def __init__(self, housepower: int):
        self.housepower = housepower
    def start(self):
        return "Engine started"
        
class Car:
    def __init__(self, make: str, model: str, housepower: int):
        self.make = make
        self.model = model
        self.engine = Engine(housepower)
        
    def start_car(self):
        return f"{self.make} {self.model} is ready. {self.engine.start()}"
        

my_car = Car("ford", "mustang", 450)
print(my_car.start_car())
        
        