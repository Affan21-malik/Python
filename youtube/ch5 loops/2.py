# for loop start 
"""
nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)
    """

"""
veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]

for val in veggies:
    print(val)

"""


"""

str = "apnacollege"

for char in str:
    print(char)

"""


"""

str = "apnacollege"

for char in str:
    print(char)
else:
    print("END")

"""




"""

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

"""



"""

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0

for el in nums:
    if el == x:
        print("number found at idx", idx)
        break
    idx += 1

"""


"""

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0

for el in nums:
    if el == x:
        print("number found at idx", idx)
    idx += 1

"""



"""

seq = range(5)

print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

"""


"""

# for i in range(10):
#     print(i)


seq = range(5)

for i in seq:
    print(i)

"""

"""
for el in range(5):
    print(el)

for el in range(1, 5):
    print(el)

for el in range(1, 5, 2):
    print(el)


"""

"""
for i in range(10):  # range(stop)
    print(i)

for i in range(2, 10):  # range(start, stop)
    print(i)


for i in range(2, 10, 2):  # range(start, stop, step)
    print(i)

"""


"""
for i in range(1, 100, 2):
    print(i)



"""

"""
n = int(input("enter number : "))

for i in range(1, 11):
    print(n * i)

"""



"""
for i in range(5):
    pass

print("some useful work")

"""

for i in range(5):
    pass
if(i>5):
    pass

print("some useful work")
