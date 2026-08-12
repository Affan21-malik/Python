
"""
#User se number lekar Even / Odd

num = int(input("enter number: "))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

"""
"""
#Largest of 3 numbers

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third is largest", c)

"""


"""
#Multiple of 7

x = int(input("enter number: "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")

"""

"""
#Largest of 4 numbers  

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))

if(a >= b and a >= c and a >= d):
    print("first number is largest", a)
elif(b >= c and b >= d):
    print("second number is largest", b)
elif(c >= d):
    print("third number is largest", c)
else:
    print("fourth number is largest", d)

"""