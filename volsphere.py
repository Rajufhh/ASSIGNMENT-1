'''
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math

radius=eval(input("Enter 1st Integer input : "))
volume=(4/3) * math.pi * (radius ** 3)
print("Volume of sphere with radius", radius, "is", volume)

