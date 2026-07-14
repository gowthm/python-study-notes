def count(limit):
    i = 0
    while i<limit:
        i+=1
        yield i

gen = count(6)

for x in gen:
    print(x)