


import math

side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))

sum_of_squares = math.pow(side_a, 2) + math.pow(side_b, 2)
hypotenuse = math.sqrt(sum_of_squares)

print(f"The hypotenuse is: {hypotenuse:.2f}")