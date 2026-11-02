#5-8 hello admin 
usernames = ['lily','ado','john','snow','amy','admin']
for username in usernames:
    if username == 'admin':
        print(f"Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
print ('\n')
#Exercise 5-9: No Users
#check if there are values in the list
usernames = ['lily','ado','john','snow','amy','admin']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
print('\n')
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
print('\n')    
#5-10. Checking Usernames
current_users = ['lily','ado','john','snow','amy','steve']
new_users= ['jame','tee','ADO','amy','pete','LILY']
current_user_lower = []
#for user in current_users:
   # current_user_lower.append(user.lower())
current_user_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_user_lower:
        print("This username has been taken. Please choose a new username")
    else:
        print("The username is available")
#5-11 ordial numbers 
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
        