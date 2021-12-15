#initalize a list (linkedlist)
student_names = ["Mike", "Amy", "Charlie", "Marco", "Leon", "Rain"]

#add a name to our list
student_names.append("Mars")
student_names.insert(0,"Mr.Amini")#insert at index (0) first position
print("first student ", student_names[0])

#delete a name
student_names.remove("Charlie")

#interate over our list
for name in student_names :
    print(name)

#get the length of the list 
length = len(student_names)
print(length)

#sort list using built in list method.sort
student_names.sort()
for name in student_names:
    print(name)







#integer list
numbers = [0, 0, 1, 1, 2, 3, 4, 0, 0, 1, 1, 0, 0, 1, 0, 0]

#count number of zeros
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)

#sort list
numbers.sort()

#print each item in list (iteration)
for number in numbers:
    print(number)


#combine two lists
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
combined_list = letters + numbers
print(combined_list)





#create a list of boolean values represent student who have done thier homework
#student who hace done thier homework
has_done_homework = [True, False, True, False, True, False]
print(has_done_homework)
has_done_homework.sort()
print(has_done_homework)


#how many falese values are in this data sturcture?
number_Falses = has_done_homework.count(False)
print(number_Falses)

#interate (tracerse the data structure)
for student in has_done_homework:
    print(student)


#make a list that stores the 
#amount of money each student has in their pocket
money_in_student_pockets = [50, 190, 4982, 4872, 587, 99, 765, 884]
print(money_in_student_pockets)
#sort the money in increasing order
money_in_student_pockets.sort()
print(money_in_student_pockets)
#add
money_in_student_pockets.append(34)
print(money_in_student_pockets)


#create a list of strings
student_names = ["Adrian", "Mike", "Charlie", "Hanson","Barbie", "Howard"]
print(student_names)
student_names.sort()
print(student_names)

