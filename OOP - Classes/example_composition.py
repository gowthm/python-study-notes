"""
Demonstrates composition ("has-a" relationship): a Car doesn't inherit
from Engine, it *contains* one and delegates work to it.
See the "Composition" section in README.md for the full explanation and diagram.
"""


class Engine:
    def __init__(self, housepower: int):
        """Store the engine's horsepower rating."""
        self.housepower = housepower

    def start(self) -> str:
        """Start the engine."""
        return "Engine started"


class Car:
    def __init__(self, make: str, model: str, housepower: int):
        """Build a Car that *has an* Engine (composition, not inheritance)."""
        self.make = make
        self.model = model
        self.engine = Engine(housepower)  # <- composition: Car HAS-A Engine

    def start_car(self) -> str:
        """Start the car by delegating to its Engine instance."""
        return f"{self.make} {self.model} is ready. {self.engine.start()}"


my_car = Car("ford", "mustang", 450)
print(my_car.start_car())  # Output: ford mustang is ready. Engine started
