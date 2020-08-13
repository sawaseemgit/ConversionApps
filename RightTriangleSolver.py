import math as m

print("Welcome to the Right Triangle Solver App")

firstSide = float(input("Enter first side of the triangle: "))
secondSide = float(input("Enter second side of the triangle: "))

hypotenuse = m.sqrt(firstSide ** 2 + secondSide ** 2)
hypotenuse = round(hypotenuse, 3)
area = round((0.5 * firstSide * secondSide), 3)

print(f'For a triangle with sides {firstSide} and {secondSide}, the hypotenuse is: {hypotenuse}')
print(f'For a triangle with sides {firstSide} and {secondSide}, the area is: {area}')
