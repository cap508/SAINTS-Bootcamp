
# The program will use mathematical operators from the maths library so we need to import them
import math

# Step 1: Get teh values form the user
side1 = input("Length of side one : ")
side2 = input("Length of side two : ")
angleDeg = input("Angle (degrees) between the two lines : ")

#Step 2: Convert strings into numeric values so we can use them in calculations
side1 = float(side1)
side2 = float(side2)
angleDeg = float(angleDeg)

# Step 3: Convert the angle from degrees to radians.
angleRad = angleDeg * math.pi/180

# Step 4: Caclulate the other side using the cosine rule
side3 = math.sqrt(side1**2 + side2**2 - 2*side1*side2*math.cos(angleRad))

#Step 5: Print out your result
print(f"The length of side 3 is {side3}")

