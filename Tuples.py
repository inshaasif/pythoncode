#Tuple is used to store multiple data.
#tuple is also take duplicate values.
#tuples are unchangeable, meaning that
#we cannot change, add or remove items after the tuple created
#tuples are created using round brackets
# Q.what if we use ',' to identify single value, it is necessary to use ',' in multiple values also??
#Q. When we print why all the values are printing??

x= ('saad', 'insha', 'raheel')
print(x)   #Tuple

class_1= ('zaid', 'sameer', 'arsalan', 'qunoot')
print(class_1)   #Tuple

class_2= ("ab", "cd", "ef", "gh", "ab", "cd", "ij")
print(class_2)    #Duplicate Values

class_3= ('zaid', 'sameer', 'arsalan', 'qunoot')
print(len(class_3))    #Tuple Length

class_4= ("apple",)
print(type(class_4))    #Type Tuple

class_5= ("apple")
print(type(class_5))   #Not Tuple
#remember When u are printing a single item the ',' is necessory.

class_6= ("saad", "insha", "raheel")
class_7= (1, 5, 7, 9, 11)
class_8= (True, False, False)

print(class_6)
print(class_7)
print(class_8)     #Data Types

class_9= ("insha", 99, "ali", True, 88)
print(class_9)     #Data Types
#Tuple can be any type Str, Int or boolean.

class_10= tuple(("anees", "raheem", "munaf"))
print(class_10)    #tuple Constructor

