#Dictionary  Basic

info = {
    "key": "value",
    "name": "apnacollege",
    "learning": "coding",
    "age": 35,
    "is_adult": True,
    "marks": 94.4
}

print(info)

#Dictionary with List and Tuple

info = {
    "name": "apnacollege",
    "subjects": ["python", "C", "Java"],
    "topics": ("dict", "set"),
    "age": 35,
    "is_adult": True,
    "marks": 94.4
}

print(info)

#Dictionary mein number ko key banana

info = {
    "name": "apnacollege",
    "subjects": ["python", "C", "Java"],
    "topics": ("dict", "set"),
    "age": 35,
    "is_adult": True,
    12.99: 94.4
}

print(info)


#Dictionary se values access karna

info = {
    "name": "apnacollege",
    "subjects": ["python", "C", "Java"],
    "topics": ("dict", "set"),
    "age": 35,
    "is_adult": True,
    12.99: 94.4
}

print(info["name"])
print(info["topics"])
print(info["subjects"])
print(info["age"])

#Dictionary mein value change/add karna


info = {
    "name": "apnacollege",
    "subjects": ["python", "C", "Java"],
    "topics": ("dict", "set"),
    "age": 35,
    "is_adult": True,
    12.99: 94.4
}

info["name"] = 23
info["surname"] = "khapra"

print(info)


#Nested Dictionary

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(student)


#Nested Dictionary se value access

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(student["subjects"]["chem"])


#keys() method

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(student.keys())


#keys() ko list mein convert karna

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(list(student.keys()))

#len() with keys()

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(len(list(student.keys())))


#values() method

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(list(student.values()))


#items() method

student = {
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(list(student.items()))


#Basic Dictionary — final small example

info = {
    "key": "value",
    "name": "apnacollege",
    "learning": "coding"
}

print(info)



#Dictionary Methods — get()

info = {
    "key": "value",
    "name": "apnacollege",
    "learning": "coding"
}

print(info.get("name"))