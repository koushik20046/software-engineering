import math

# Keyboard input
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Two roots: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"One root: {root}")
else:
    print("No real roots")
