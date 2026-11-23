max_value = -1

value = int(input())

while value != 0:
    if value > max_value:
        max_value = value

    value = int(input())

print(max_value)
