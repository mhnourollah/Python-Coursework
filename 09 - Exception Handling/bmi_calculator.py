try:
    weight = int(input("Weight: "))
    height = int(input("Height: "))

    bmi = (weight / (height * height)) * 703

    print(bmi)

except ValueError:
    print("Could not calculate health info.")
