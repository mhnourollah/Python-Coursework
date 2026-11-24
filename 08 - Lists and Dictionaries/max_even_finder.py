nums = [3, 5, 23, -1, 456, 1, 6, 83]

max_even = None

for num in nums:
    if num % 2 == 0:
        if max_even is None or num > max_even:
            max_even = num

print(max_even)
