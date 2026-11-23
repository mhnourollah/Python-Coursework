password = "star"

user_input = input("Enter password: ")

while user_input != password:
    print("Wrong password")
    user_input = input("Enter password: ")

print("Access granted")
