"""Basic CRUD (Create, Read, Update, Delete) operations on a dictionary."""

product = {
    "id": "SKU-234",
    "name": "Wireless mouse",
    "price": 299.9,
    "stock": 100
}

# Read
print(product['name'])

# Update
product['price'] = 234.45

# Delete
product.pop('stock')
