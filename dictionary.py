#Dictionaries or Hashamps have fast lookup due to how they're store in memory

#create a dictionary(key-value pairs) aka "HashMap, Map, HashTable"
assignment_scores = {"Mars":90,"Amy":93, "Rain":98, "Charlie":98}
amy_assignment_stores = assignment_scores.get("Amy")
print("Amy assignment score", amy_assignment_stores)

#create a dictionary using built in dict function(same thing, different way to write it)
exam_scores = dict(Mars = 90, Amy = 93, Rain = 98, Charlie = 98)
mars_scores = exam_scores.get("Mars")
print("Mars exam score",mars_scores)








#key - student name 
has_pets = { "Mar":False, "Henry":False, "Barbile":True, "Adrian":False, "Angelina":False }

#data structure operations - add, delete, search, sort
student_has_pet = has_pets.get("Mars")
print("The student has a pet:",student_has_pet)

#tranverse the dictionary
for student in has_pets:
    print(student, "has a pet:",has_pets.get(student))

#remove method - pop()
student_removed = has_pets.pop("Adrian")
print(student_removed)
print(has_pets)


#create a dictionary(key-value pair)
#key = student name
#value = list of scores(numbers)

student_scores = {"Adrian":[90,91,88],"Charlie":[88,99,100],"Mandy":[90,95,99],"Yujing":[100,99,95],"Angelina":[99,98,99],"Mr.Amini":[50,99,99],"Howard":[99,100,97]}

student_scores = student_scores.get("Howard")
for score in student_scores:
    print(score)


student_siblings = {"Howard":["Barbie","Anthony","Annie"],"Barbie":["Howard","Anthoy","Annie"],"Adrian":["girl_Adrian","another_gitl_Adrian","boy_Adrian0"],"Mike":["Angel"],"Yujing":["Jimmy"]}
student_brothers_sisters = student_siblings.get("Howard")
student_brothers_sisters.sort()
for sibling in student_brothers_sisters:
    print(sibling)
