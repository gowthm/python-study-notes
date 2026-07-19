class Camera:
    def take_photo(self) -> str:
        return "Photo captured successfully"


class Phone:
    def make_call(self) -> str:
        return "Dialing..."


class Smartphone(Camera, Phone):
    def browse_internet(self) -> str:
        return "Loading browser..."


# Instantiate child class and invoke inherited and class methods
my_phone = Smartphone()

print(my_phone.take_photo())
print(my_phone.make_call())
print(my_phone.browse_internet())