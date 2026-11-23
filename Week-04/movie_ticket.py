age = int(input("Enter age: "))

if age <= 12:
    price = 11
elif age >= 65:
    price = 12
else:
    price = 14

print(f"Ticket price: ${price}")
