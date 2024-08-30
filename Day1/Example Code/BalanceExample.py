boundaries = [40, 50, 60, 70, 80]
result = ["3rd", "2:2", "2:1", "1st", "Distinction"]

grade = input("Please enter the grade as an integer : ")

if (int(grade) > boundaries[4]):
   print(f"Your result is a {result[4]}")
elif (int(grade) > boundaries[3]):
   print(f"Your result is a {result[3]}")
elif (int(grade) > boundaries[2]):
   print(f"Your result is a {result[2]}")
elif (int(grade) > boundaries[1]):
   print(f"Your result is a {result[1]}")
elif (int(grade) > boundaries[0]):
   print(f"Your result is a {result[0]}")
else: 
   print("Your failed your exam")