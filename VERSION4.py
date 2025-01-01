import math
import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# Read values from file
with open('input.txt', 'r') as file:
    for line in file:
        a, b, c = map(float, line.split())

        # Calculate discriminant
        discriminant = b**2 - 4*a*c

        # Roots of the quadratic equation
        roots = []
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            roots = [root1, root2]
            print(f"Equation: {a}x^2 + {b}x + {c} = 0")
            print(f"Two roots: {root1}, {root2}")
        elif discriminant == 0:
            root = -b / (2 * a)
            roots = [root]
            print(f"Equation: {a}x^2 + {b}x + {c} = 0")
            print(f"One root: {root}")
        else:
            print(f"Equation: {a}x^2 + {b}x + {c} = 0")
            print("No real roots")

        # Graphical representation
        x = np.linspace(-10, 10, 500)  # Generate x values
        y = a * x**2 + b * x + c       # Quadratic equation

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
        plt.axhline(0, color='black', linewidth=0.8)  # x-axis
        plt.axvline(0, color='black', linewidth=0.8)  # y-axis

        # Mark roots if they exist
        if roots:
            for root in roots:
                plt.scatter(root, 0, color='red', zorder=5)
                plt.text(root, 0.5, f'({root:.2f}, 0)', color='red')

        # Titles and labels
        plt.title(f'Graph of {a}x² + {b}x + {c}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()
