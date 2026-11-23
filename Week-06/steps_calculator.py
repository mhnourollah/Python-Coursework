def steps_to_feet(num_steps):
    return num_steps * 3

def steps_to_calories(num_steps):
    return (num_steps / 70) * 3.5

steps = int(input())

print("Feet:", steps_to_feet(steps))
print("Calories:", steps_to_calories(steps))
