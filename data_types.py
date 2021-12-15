
#key - student name 
has_pets = { "Mar":False, "Henry":False, "Barbile":True, "Adrian":False, "Angelina":False }

#data structure operations - add, delete, search, sort
student_has_pet = has_pets.get("Mars")
print("The student has a pet:",student_has_pet)

#tranverse the dictionary
for student in has_pets:
    print(student, "has a pet:",has_pets.get(student))