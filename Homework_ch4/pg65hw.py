players = ["charles", "martina", "michael", "florence", "eli", "sarah", "david"]
print(f"The first 3 items in this list are:")
print(players[0:3])
print(players[2:5])
print(players[-4:-1])
my_pizzas=["cheese pizza", "pepperoni pizza", "veggie pizza"]
friend_pizza =my_pizzas[:]
my_pizzas.append("mushroom pizza")
friend_pizza.append("pineapple apple")
print(f'\nMy favourite pizzas are:')
for pizza in my_pizzas:
    print(pizza)
print(f'\nHis favourite pizzas are:')
for pizza in friend_pizza:
    print(pizza)