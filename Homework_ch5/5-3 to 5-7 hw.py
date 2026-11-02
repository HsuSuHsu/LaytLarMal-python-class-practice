alien_color = 'green'
if alien_color == 'green':
    print(f"You've just earned 5 points!")
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
#5-4 alien colour 2
alien_color = 'yellow'
if alien_color == 'green':
    print(f"\nYou've just earned 5 points for shooting the alien!")
else:
    print(f"\nYou've just earned 10 points for shooting the alien!")
#5-5. Alien Colors #3:
alien_color = 'red'
if alien_color == 'green':
    print(f"\nYou've just earned 5 points for shooting the alien!")
elif alien_color == 'yellow':
    print(f"\nYou've just earned 10 points for shooting the alien!")
else:
    print(f"\nYou've just earned 15 points for shooting the alien!")

#5-6. Stages of Life
person_age = 27
if person_age <2:
    print(f"\nThis person is a baby")
elif person_age >= 2 and person_age < 4:
    print(f"\nThis person is a toddler")
elif person_age >=4 and person_age <13:
    print(f"\nThis person is a kid")
elif person_age >=13 and person_age <20:
    print(f"\nThis person is a teenager")
elif person_age >=20 and person_age <65:
    print(f"\nThis person is an adult")
elif person_age >=65:
    print(f"\nThis person is an elder")

#other way or better version of if-elif-else chain
person_age = 86

if person_age < 2:
    print("This person is a baby")
elif person_age < 4:
    print("This person is a toddler")
elif person_age < 13:
    print("This person is a kid")
elif person_age < 20:
    print("This person is a teenager")
elif person_age < 65:
    print("This person is an adult")
else:
    print("This person is an elder")
#5-7 
favourite_fruits =['strawberry','banana','kiwi']
if 'strawberry' in favourite_fruits:
    print(f"\nI really love strawberry.")
if 'mango' in favourite_fruits:
    print(f"\nI really love mango")
if 'kiwi' in favourite_fruits:
    print(f"\nI really love kiwi")
if 'apple' in favourite_fruits:
    print(f"\nI really love apple")