try:
    divisor = int(input())

    print(60 // divisor)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")
