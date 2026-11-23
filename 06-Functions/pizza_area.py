import math

def calc_pizza_area(diameter):
    radius = diameter / 2
    return math.pi * radius * radius

print(calc_pizza_area(12))
