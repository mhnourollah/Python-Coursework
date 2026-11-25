f = open("mydata.txt")

lines = f.readlines()

f.close()

total = 0

for line in lines:
    total += int(line)

avg = total / len(lines)

print(avg)
