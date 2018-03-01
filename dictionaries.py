fruit = {"orange": "a sweet, orange, citrus",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in",
          "lime": "a sour, green citrus fruit"}

print (fruit)
print (fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
