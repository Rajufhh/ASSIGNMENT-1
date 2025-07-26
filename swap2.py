'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
try:
    x = eval(input("Enter 1st input : "))
    y = eval(input("Enter 2nd input : "))
    temp= x
    x = y
    y = temp
    print("After swap : x =", x, "and y =", y)
except :
    print("Enter String input in Quotes")