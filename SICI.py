'''
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''

import math
principle = eval(input("Enter principle amount : "))
time = eval(input("Enter time in years : "))
rate = eval(input("Enter rate of interest : "))

simple_interest = (principle * time * rate) / 100
compound_interest = principle * (1 + rate / 100) ** time - principle

print("Simple Interest :", simple_interest)
print("Compound Interest :", compound_interest)