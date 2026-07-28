"""
Demonstrates the @property decorator: horsepower is exposed as a normal
attribute (my_car.horsepower) but every read/write is secretly routed
through a getter/setter pair that validates the value.

See property.md for the full write-up and diagram.
"""


class Car:
    def __init__(self, make: str, horsepower: int):
        """Create a Car and set horsepower through the validating setter below."""
        self.make = make
        self.horsepower = horsepower  # goes through the setter, not a plain assignment

    @property
    def horsepower(self) -> int:
        """Getter: runs on `car.horsepower` (read access)."""
        return self._horsepower

    @horsepower.setter
    def horsepower(self, value: int) -> None:
        """Setter: runs on `car.horsepower = value` (write access).

        Raises:
            ValueError: if value is negative.
        """
        if value < 0:
            raise ValueError("Horsepower should be a positive value")
        self._horsepower = value


my_car = Car("ford", 450)

print(my_car.horsepower)  # Output: 450

my_car.horsepower = -200  # Output: raises ValueError("Horsepower should be a positive value")
