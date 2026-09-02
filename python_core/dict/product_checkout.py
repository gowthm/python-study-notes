"""A mini shopping-cart checkout simulation using dictionaries."""

product = {
    "laptop": 266.1,
    "mouse": 34.12,
    "keyboard": 44.9,
    "monitor": 100,
    "speaker": 44.55
}

overall_card = {}


def add_product(item, qty):
    """Add `qty` units of `item` to the cart, ignoring items not in stock."""
    item = item.lower()
    if item in product:
        overall_card[item] = overall_card.get(item, 0) + qty
    else:
        print('This item is not available')


def checkout():
    """Print the total price of everything currently in the cart."""
    final_price = 0
    for item, count in overall_card.items():
        price = product[item]
        rate = price * count
        final_price = final_price + rate
    print("Final Price:", final_price)


add_product('Laptop', 1)
add_product('mouse', 2)
add_product('keyboard', 1)
add_product('phone', 2)   # Output: This item is not available
add_product('laptop', 2)
checkout()                # Output: Final Price: 911.44
