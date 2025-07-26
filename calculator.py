'''Enter 1st Integer number :  10
Enter 2nd  integer  number :  7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd(10 , 7) = 1
fact(10) = 3628800'''
import math 

n=eval(input("Enter 1st Integer number :"))
m=eval(input("Enter 2nd Integer number :"))

print(n,"+",m,"=",n+m)

print(n,"-",m,"=",n-m)

print(n,"*",m,"=",n*m)

print(n,"/",m,"=",n/m)

print(n,"%",m,"=",n%m)

print("max(",n,",",m,")","=",max(n,m))

print("min(",n,",",m,")","=",min(n,m))

print(n,"^",m,"=",n**m)

print("sqrt(",n,")","=",math.sqrt(n))

print("gcd(",n,",",m,")","=",math.gcd(n,m))

print("fact(",n,")","=",math.factorial(n))




