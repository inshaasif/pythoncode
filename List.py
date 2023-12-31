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

list_4= ["insha", "raheel", "saad"]
for x in list_4:
    print(x)       #Loop List

list_5= ["anas", "arqam", "ahsan"]
for i in range(len(list_5)):
    print(list_5[i])        #Loop Through Index

list_6= ["safwan", "azhan", "rohail"]
i= 0
while i < len(list_6):
    print(list_6[i])
    i = i + 1        #While Loop

list_7= ["hameed", "raheem", "faheem"]
[print(x) for x in list_7]      #List Comprehension Looping

list_8= ["apple", "banana", "cherry", "Kiwi", "mango"]
newlist= []
for x in list_8:
    if "a" in x:
        newlist.append(x)
print(newlist)       #List Comprehension

list_9= ["Dell", "Hp", "Lenovo", "Sony"]
newlist= [x for x in list_9 if x != "Dell"]
print(newlist)      #Condition

list_10= [x for x in range(10)]
print(list_10)      #Iterable

newlist= [x for x in range(10) if x < 5]
print(newlist)      #same example with condition

list_11= ["graphics", "animation", "designing"]
newlist= [x.upper() for x in list_11]
print(newlist)      #Expression

list_12= ["graphics", "animation", "designing"]
newlist= ['hello' for x in list_12]
print(newlist)   #same example with condition

list_13= ["ameen", "raheem", "saleem", "kareem"]
newlist= [x if x != "raheem" else "faheem" for x in list_13]
print(newlist)     #same example with condition


list_14= ["shahmir", "hammad", "khalid", "suleman", "arham"]
list_14.sort()
print(list_14)        #sort (sort alphabetically)

list_15= ["88", "45", "97", "21", "66"]
list_15.sort()
print(list_15)        #sort (sort numerically)

list_16= ["88", "45", "97", "21", "66"]
list_16.sort(reverse = True)
print(list_16)        #Descending 

def myfunc(n):
    return abs(n - 500)

list_17= [88, 45, 50, 97, 21, 66] 
list_17.sort(key= myfunc)
print(list_17)      #Customize Sort Function 
 
list_18= ["shahmir", "Hammad", "Khalid", "suleman", "Arham"]
list_18.sort()
print(list_18)    #case Insensitive

list_19= ["Anydesk", "Facebook", "Github", "google", "yahoo"]
list_19.sort(key= str.lower)
print(list_19)   #Case insensitive (lower)

list_20= ["Pakistan", "India", "SriLanka", "Bangladesh"]
list_20.reverse()
print(list_20)    #Reverse Order

list_21= ["23", "33", "44", "65"]
mylist = list_21.copy()
print(mylist)    #Copy List

list_22= ["elephant", "lion", "tiger", "cat"]
mylist= list(list_22)
print(mylist)    #Another way of copy list

Var_1= ["art", "cart", "part"]
var_2= ["12", "25", "35"]
var_3= Var_1 + var_2
print(var_3)      #Join List

Var_4= ["a", "b", "c"]
var_5= ["1", "2", "3"]

for x in var_5:
    Var_4.append(x)

print(Var_4)     #Another way of join list (append)

var_6= ["arqam", "arham", "aslam", "zaid"]
var_7= ["22", "41", "99", "13"]

var_6.extend(var_7)
print(var_6)      #Another way of join list (extend)

