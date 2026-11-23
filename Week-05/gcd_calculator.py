num_a = int(input())
num_b = int(input())

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
    else:
        num_b = num_b - num_a

print("GCD:", num_a)
