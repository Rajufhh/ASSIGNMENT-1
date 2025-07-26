#LARGEST AMONG THREE NUMBERS

try:
    a=eval(input("Enter 1st  input : "))
    b=eval(input("Enter 2nd  input : "))
    c=eval(input("Enter 3rd  input : "))
    
    print("Largest Number :",a if a>b and a>c else b if b>c and  b>a else c)
except:
    print("Enter String input in Quotes")
    


