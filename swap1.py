'''Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects'''

try:
    n=eval(input("Enter 1st  input : "))
    m=eval(input("Enter 2nd  input : "))
    print("Before swapping:")
    print("x =",n)
    print("y =",m)
    
    n,m=m,n  # Swapping in a single statement

    print("After swapping:")
    print("x =",n)
    print("y =",m)
except:
    print("Enter String input in Quotes")
