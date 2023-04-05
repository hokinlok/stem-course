#!/usr/bin/env python3
upper_base = 6
lower_base = 8
height = 9
area = (upper_base + lower_base) * height / 2
result = "The area of the trapezium is " + str(area) + " cm^2"
print(result)
# The area of the trapezium is 63.0 cm^2


side_1 = 7
side_2 = 7
side_3 = 7
side_4 = 7
if side_1 == side_2 and side_2 == side_3 and side_3 == side_4:
  print("It is a square!")
elif side_1 == side_3 and side_2 == side_4:
  print("It is a rectangle!")
else:
  print("It is a quadrilateral.")
# It is a square!
