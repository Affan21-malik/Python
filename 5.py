"""
str1 = "This is a string.\twe are creating it in python."
print(str1)

# tab space\t ro \n new line  k liye 
"""
"""

#String Concatenation +
str1 = "apna"
str2 = "college"

print(str1 + str2)
"""


"""
#String ki length
str1 = "apna"
len1 = len(str1)
print(len1)

"""

"""
#Indexing
str = "apna college"
ch = str[0]
print(ch)

"""


"""
#Slicing 

str = "apna college"
print(str[0:4])

print(str[5:len(str)])

print(str[:4])  #Means:str[0:4]

print(str[5:])  #Means:str[5:len(str)]
"""

"""
#Negative indexing

str = "apple"
print(str[-5:-2])


# String:   a    p    p    l    e
# Index:   -5   -4   -3   -2   -1

"""


"""
#check karta hai ki string given text se end ho rahi hai ya nahi.
str = "I am studying python from ApnaCollege"
print(str.endswith("ege"))

"""



"""
#sirf first character ko uppercase karta hai aur baaki characters ko lowercase kar deta hai.

str = "i am studying python from ApnaCollege"
print(str.capitalize())

"""



"""
#Ye string ke saare o ko a se replace karega.

str = "i am studying python from ApnaCollege"
print(str.replace("o", "a"))

"""



"""
# Yahan first "from" index 5 par hai.

# Output:

# 5



str = "i am from studying python from ApnaCollege"
print(str.find("from"))

"""



"""
# String me "from" 2 baar hai.

# Output:

# 2



str = "i am from studying python from ApnaCollege"
print(str.count("from"))




"""



