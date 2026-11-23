factorial = int(input())

count = factorial - 1

while count >= 1:
    factorial *= count
    count -= 1

print(factorial)
