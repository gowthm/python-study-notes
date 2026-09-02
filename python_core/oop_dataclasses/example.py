from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Product:
    id: int
    name: str
    price: float

    def __str__(self) -> str:
        return f"{self.name} - ${self.price}"


@dataclass
class Customer:
    id: int
    name: str


@dataclass
class Order:
    id: int
    customer: Customer
    product: Product
    quantity: int


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class UPI(Payment):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using UPI")


# Instantiate dataclasses and simulate an order/payment flow
product = Product(id=1, name="Laptop", price=65000.0)
customer = Customer(id=101, name="Alice")
order = Order(id=500, customer=customer, product=product, quantity=2)

print(product)
print(order)

payment = UPI()
payment.pay(product.price * order.quantity)
