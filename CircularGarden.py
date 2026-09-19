import math

# --- Circular Garden ---

    # Ask for the radius of the garden:
radius = float(input("Enter the radius of the garden: "))

    # Calculate the area and circumference using the radius given by the user:
area =  math.pi * (math.pow(radius, 2))

circumference = 2 * math.pi * (radius)

    # Find the square root of the calculated area
sqrt = math.sqrt(area)

    # Determine the area rounded up and down to the nearest whole number:
areaRoundedDown = math.floor(area)
areaRoundedUp = math.ceil(area)

    # Display the area, circumference, and square root of the area
print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circumference:.2f} meters")
print(f"Square root of the area: {sqrt:.2f}")
print(f"Area rounded down: {areaRoundedDown:.2f} square meters")
print(f"Area rounded up: {areaRoundedUp:.2f} square meters")