class_1= ["abdullah", "noman", "raheel"]
print(class_1)   #list

class_2= ["insha", "Haris", "arqam", "Haris", "insha"]
print(class_2)    #allow dulicates

class_3= ["asad", "umer"]
print(len(class_3))     #len

class_4= ["abdullah", "noman", "raheel"]
class_5= [1, 5, 9, 7, 8]
class_6= [True, False, False]
print(class_4)
print(class_5)
print(class_6)    #Data Types

list_1= ["karachi", "lahore", "sialkot"]
print(type(list_1))    #type ()
list_2= ["insha", 44, True, 90, "saad"]
print(type(list_2))    #type()

class_7=list(("apple", "banana", "peach"))
print(class_7)    #list constructor()

class_8= ["abdullah", "noman", "raheel"]
print(class_8[1])    #Access List

class_9= ["ahmed", "huzaifa", "waqas", "zaid"]
print(class_9[-2])   #negative Index

class_10= ["kiwi", "apple", "banana", "coconut", "peach", "watermelon"]
print(class_10[2:5])
class_10= ["kiwi", "apple", "banana", "coconut", "peach", "watermelon"]
print(class_10[:4])
class_10= ["kiwi", "apple", "banana", "coconut", "peach", "watermelon"]
print(class_10[2:])     #Range Indexes

class_11= ["arsalan", "safdar", "shehroz", "bilal", "uzair", "rehan"]
print(class_11[-5:-1])  #negative Indexes(range)

class_12= ["raheel", "saad", "insha"]
if "raheel" in class_12:
    print("yes, 'raheel' is present")   #Check Item Exist

class_13= ["Bat", "Hat", "Cat"]
class_13[1]= "Rat"
print(class_13)     #change Item value

class_14= ["anas", "waqas", "aqil", "aqib", "rashid", "babar"]
class_14[1:3]= "amin", "anees"
print(class_14)    #change Range Items

class_15= ["potato", "tomato", "ladyfinger"]
class_15[1:3]= ["onion"]
print(class_15)    #replacing with one value

class_16= ["Karachi", "Lahore", "Sawaat", "sialkot"]
class_16.insert(2, "Hyderabad")
print(class_16)     #Insert Item

class_17= ["pakistan", "sriLanka", "Bangladesh", "India"]
class_17.append("Nepal")
print(class_17)    #Add Items

class_18= ["Java", "Python", "CSS"]
class_18.insert(1, "Php")
print(class_18)     #Insert Item

class_19= ["apple", "coconut", "rasberry"]
class_20= ["blueBerry", "orange", "Guava"]
class_19.extend(class_20)
print(class_19)     #extend List

var= ["sun", "moon", "star"]
var.remove("moon")
print(var)   #Remove Items

list_1= ["pakistan", "sriLanka", "Bangladesh", "India"]
list_1.pop(2)
print(list_1)     #Pop() remove specified Index

list_2= ["apple", "coconut", "rasberry"]
del list_2[1]
print(list_2)      #del is also remove specified index

list_3= ["sun", "moon", "star"]
list_3.clear()
print(list_3)        #clear List