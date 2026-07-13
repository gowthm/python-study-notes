fruits = ["apple", "banana", "apple", 'cherry', 'apple']
count = {}

for fruit in fruits:
    count[fruit] = count.get(fruit, 0)+1
    
print(count)