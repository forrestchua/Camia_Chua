# HYPOTENUSE OF A RIGHT TRIANGLE

## Description
 This program helps you in finding the hypotenuse of a right triangle.

## How to Run:
- Open the code in Python
- Run the Python file
- Input the desired numbers

## Input Needed
- side_a
- side_b

## Sample Output

import math

side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))

sum_of_squares = math.pow(side_a, 2) + math.pow(side_b, 2)
hypotenuse = math.sqrt(sum_of_squares)

print(f"The hypotenuse is: {hypotenuse:.2f}")

## Author
Name: Forrest Zelline M. Chua
Section: 8-Camia
