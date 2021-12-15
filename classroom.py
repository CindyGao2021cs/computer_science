#arithentic operations 
# write code to complete the following arithmetic poerations
#print the results on the screen


1 + 5
99999 - 9494
38484 * 999
24 / 2
90 % 10

a = 1
b = 5
c = a + b
print(c)

a = 99999
b = 9494
c = a - b
print(c)

a =38484
b = 999
c = a * b
print(c)


a = 24
b = 2
c = a / b
print(c)




#there are 21 computer science students, each student has $15.5 dollars
#how much money does the class have in total

computer_science_students = 21
each_student_has = 15.5
total = computer_science_students * each_student_has
print(total)

#string operations
alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
#write a line of code to find the lengh of this string
#print the lengh on the screen


#write code th find the index (position) of the letter "t"
#print the index on the screen 

position = alphabet.find('t')
print(position)










#string are objects in python
#using the dot operator(.)we can access an object's functions (methods)
message = "this is my message"
uppercase_message = message.upper()
print(uppercase_message)

#len function isn't a part of the string object it's more "general"
#that's why it's not called using the dot operator message.len()
lenght = len(message)

#for loop
for i in range(8):
    print("this is confusing",i)

#while loop
counter = 0
while(counter < 10):
    print("Iknow computer science",counter)
    cornter = counter + 1

working = True
while(working == True):
   print("working")
   working = False




#try-catch block 
try: 
    age = int(input("Enter your age:"))
    calculation = 10/


#data validation - length check
password = input("enter a password:")

password_length = len(password)

if(password_length < 7 or password_length > 15):
    print("yourpassword must be between 7-15 characters")

#data validation - admin password 
adnim_password = input("enter your new password:")
admin_password_length = len(



#check if user enters an empty string

name_length = len(name)

if(name_length = 0):
    print("youcannot enter an empty name")
elif(name_length < 3):
    print("name must be more than three letters")
elif(name_length > 25):
    print("name must be less than 25 characters")



#write a program that takes a new pet name and validates its length 
#in other words, it prints an error message to the if...
#the name is less than 2 chars and greater than 20 chars
# 2 < name =< 20


#outline the steps - algorithm
#ask user for pet name, store it in a variable
#use fn to get pet name length, store length in a new variable
#validate - if-elif to print error messages if len is outside boundaries

#1. ask user for pet name
pet_name = input("enter your pet name:")

#2. get pet name length
pet_name_length = len(pet_name)

#3. validate length + display messages to user
if(pet_name_length = 0):
    print("you are must enter something")
elif(pet_name_length < 2):
    print("your pet must have a name weth more than 2 letters")
elif(pet_name_length >= 20):
    print("enter a name that in less than or equal to 20 letters")




#create a list of boolean values represent student who have done thier homework
#student who hace done thier homework
has_done_homework = [True, False, True, False, True, False]
print(has_done_homework)
has_done_homework.sort()
print(has_done_homework)
