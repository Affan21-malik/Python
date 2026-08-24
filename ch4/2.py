
#.get() — key nahi mile to error nahi
student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}


#  print(student["name2"])      name2 dictionary mein hai hi nahi, isliye error (KeyError) aayega.

print(student.get("name2")) #.get() ka fayda: key missing hone par program error nahi deta, None return karta hai.



# .update() — dictionary mein new key add/change

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

student.update({"city": "delhi"})



#Existing key ko update karna

new_dict = {
    "name": "neha kumar",
    "age": 16
}

student.update(new_dict)


"""

student["name"]	Key nahi mili → ❌ Error
student.get("name")	Key nahi mili → None
student.update({...})	New key add / old value update  


"""
