user_age = int(input("Enter your age: "))

if user_age < 16:
    insurance_price = 0
elif user_age < 25:
    insurance_price = 4800
elif user_age < 40:
    insurance_price = 2350
else:
    insurance_price = 2100

print(f"Annual price: ${insurance_price}")
