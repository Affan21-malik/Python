"""
# A,B="2",3
# Text="@"
# print((A+Text)*B)

C,D=2,3
Text="@"
print(C*D*Text)

A,B=10,5.0
print(A*B)
A,B=1.5,3
c=A//B
print(c,A/B)# // ye float value minimum int badal deta h like 0.5 ,0 krdiye   chota or equal wala lenge int bhi o bda nhi lenge
#   like 0.99 k int 0 or 1.99 ya 1.1 ye bhi int 1 or -0.59 k hoga -1 or -2.56 bhi -3 hoga


# numerator     +  - + -
#denominator    +  - - +
#ans value hogi +  + - +  ye vlaye btada modulu krna pr positive agi ya negative 

"""




"""
name= input( "name :")
print(name)

age=int(input("age:"))
print(age)

price=float(input("price:"))
print(price)"""





"""
name= input( "name :")
age=int(input("age:"))
price=float(input("price:"))

print(" my name is ",name," and i am ",age,"old")"""







"""
light = input("light : ")

if (light == "red"):
    print("stop")

elif (light == "yellow"):
    print("look")

elif (light == "green"):
    print("go")

else:
    print("light is broken")"""







marks = int(input("marks : "))

if (marks >= 90):
    print("A")

elif (marks >= 80 and marks < 90):
    print("B")

elif (marks >= 70 and marks < 80):
    print("C")

else:
    print("D")