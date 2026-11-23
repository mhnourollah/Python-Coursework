daily_revenues = [
    2350.25,
    1800.50,
    1795.00,
    2050.25,
    1985.75,
    2005.00,
    1890.50
]

total = 0

for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print(total)
print(average)
