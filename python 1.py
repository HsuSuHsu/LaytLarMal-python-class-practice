print("hello world")
message = ("hello world")
print(message)
message = ("hello python world")
print(message)
first_name = "ada"
last_name = "lace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"My name is {first_name.title()}{last_name.title()}")
print(f"My name is {first_name.title()} {last_name.title()}")
print("\tpython")
print("Languages:\npython\nJava\nCplus")
my_languages = """Languages:
python
java
Cplus"""
print(my_languages)
fruit = "Straw\\berry"
print(fruit)
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))
age  = 140_000
print(age)
# hi guys 
# ladies
# hahaha
x = 5
print (x)
x= x+3
print (x)
x-=3
print(x)
y = 5
print (x==y)
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
print(fruits[1:3])
print(fruits[:])
print(fruits[-3:-1])
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[::2])
print(numbers[::-1])
numbers[2]=10
print(numbers)
fruits.append("banana")
print(fruits)
fruits.insert(1,"berry")
print(fruits)
fruits.append("coconut")
print(fruits)
fruits.insert(3,"pineapple")
print(fruits)
more_fruits = ["aa", "rr","coconut"]
fruits.extend(more_fruits)
print(fruits)
fruits.remove("coconut")
print(fruits)
del fruits[0:3]
print(fruits)
popped_fruit = fruits.pop(1)
print(fruits)
print(popped_fruit)
print(f"The fruit I like the most is {popped_fruit.capitalize()}")
fruits.clear()
print(fruits)
cars=["suzuki","honda","nissen","toyota"]
print("toyota" in cars)
print("hilux" in cars)
cars.sort()
cars.reverse()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(len(cars))
for car in cars:
    print(car)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'This was a good idea, {magician.title()}!')
    print(f"I can't wait to see you,{magician.title()}.\n")
for value in range(1,5):
    print(value)
numbers = list(range(1,5))
print (numbers)
even_numbers = list(range(2,11,2))
print (even_numbers)
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
squares=[value**2 for value in range(1,11)]
print (squares)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the player on my team:")
for player in players[:3]:
    print(player.capitalize())
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food=my_foods[:]
print(friend_food)
my_foods.append("apple")
friend_food.append("orange")
print(my_foods)
print(friend_food)
#tuple dimensions, using parentheses instead of []
dimensions=(200,50)
print(dimensions[0])
dimensions=(400,200)
print(dimensions)