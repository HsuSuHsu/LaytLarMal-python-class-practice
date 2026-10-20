#3-4
guest_list=["amy","peter","ian","lily"]
for guest in guest_list:
    print(f"Hi {guest.title()}, I would like to invite you to dinner.")
#3-5
print(f"\n{guest_list[1].title()} can't come to the dinner")
del guest_list[1]
guest_list.insert(1,"felix")
print(f"Hi {guest_list[1].title()}, I would like to invite you to dinner\n")
#3-6.
print(f"I've found a bigger table for the dinner! We can invite more people.\n")
guest_list.insert(0,"Kim")
guest_list.insert(2,"Jim")
guest_list.append("Katy")
for guest in guest_list:
    print(f"Hey {guest.title()}, I would like to invite you to dinner")
print(guest_list)
print(f"I'm sorry. I can only invite two people to dinner\n")
uninvited_guest=guest_list.pop(0)
uninvited_guest=guest_list.pop(0)
uninvited_guest=guest_list.pop(0)
uninvited_guest=guest_list.pop(0)
uninvited_guest=guest_list.pop(0)
for guest in guest_list:
    print(f"{guest.title()}, you are still invited!")
del guest_list[:]
print(guest_list)
