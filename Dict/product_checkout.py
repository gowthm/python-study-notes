product = {
    "laptop": 266.1,
    "mouse": 34.12,
    "keyboard": 44.9,
    "moniter": 100,
    "speaker": 44.55
}

overall_card = {}

def add_product(item, qty):
    item = item.lower()
    if item in product:
        overall_card[item] = overall_card.get(item, 0) + qty
    else:
        print('This item not available')
    
def checkout():
    final_price = 0
    for item,count in overall_card.items():
        price = product[item]
        rate = price*count
        final_price = final_price + rate
    print("Final Price:", final_price)
        

add_product('Laptop', 1)
add_product('mouse', 2)
add_product('keyboard', 1)
add_product('phone', 2)
add_product('laptop', 2)
checkout()    