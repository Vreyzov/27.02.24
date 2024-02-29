import math

def circle_length(radius):
    return 2 * math.pi * radius

def circle_area(radius):
    return math.pi * radius**2

def main():
    radius = float(input("Введите радиус окружности: "))
    length = circle_length(radius)
    area = circle_area(radius)
    print(f"{length} {area}")