#Data Types Lecture
computer_science_students = 21#this is an integer value
has_done_homework = True #this is a boolean value
class_name = "IGCSE Computer Science" #this is a string value

#we can now access this data by the variable name
print(computer_science_students)
print(has_done_homework)
print(class_name)





#validation task - write code that takes user input and validates its length
#ask the user for a restaurant name
#validate that the name is greater than 5 letters and less than 25 letters

#1 - get name of restaurant
resturant_name = input("Enter a restaruant name:")
#2 - get length
restaurant_name_length = len(resturant_name)
print(restaurant_name_length)
#3 - validation
if(restaurant_name_length = 0):
    print("youmust enter something")
elif(restaurant_name_length < 5):
    print("you must enter a name with more than five letters")
elif(restaurant_name_length > 55):
    print("you must enter a name with less than 25 letters")