#!/usr/bin/env python3
base = 6
height = 9
area = base * height / 2
result = "The area of the triangle is " + str(area) + " cm^2"
print(result)
# The area of the triangle is 27 cm^2


side_1 = 7
side_2 = 7
side_3 = 7
if side_1 == side_2 and side_2 == side_3:
  print("It is an equilateral triangle!")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
  print("It is an isosceles triangle!")
else:
  print("It is a triangle.")
# It is an equilateral triangle!
