"""
Demonstrates multiple inheritance: Smartphone inherits from BOTH Camera
and Phone, gaining all of their methods in addition to its own.
See method_resolution_order.md for how Python resolves conflicts
when parent classes share a common method name.
"""


class Camera:
    def take_photo(self) -> str:
        """Capture a photo."""
        return "Photo captured successfully"


class Phone:
    def make_call(self) -> str:
        """Place a phone call."""
        return "Dialing..."


class Smartphone(Camera, Phone):
    """Inherits from both Camera and Phone (multiple inheritance)."""

    def browse_internet(self) -> str:
        """Load a web page."""
        return "Loading browser..."


# Instantiate the child class and invoke both inherited and own methods
my_phone = Smartphone()

print(my_phone.take_photo())      # Output: Photo captured successfully   (from Camera)
print(my_phone.make_call())       # Output: Dialing...                   (from Phone)
print(my_phone.browse_internet()) # Output: Loading browser...           (own method)
