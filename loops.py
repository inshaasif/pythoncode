#Points for loops

#for: This keyword is used to start the loop.
#item: This is a variable that takes on the value of each element in the iterable during each iteration of the loop. You can choose any valid variable name.
#in: This keyword is used to specify the iterable that you want to loop through.
#iterable: This is the sequence or collection you want to iterate over. It could be a list, tuple, string, range, dictionary keys, and other iterable objects.
# "for loop" is a fundamental construct in Python programming and is used extensively for various tasks that involve iterating over data structures.
#It allows you to perform repetitive tasks efficiently by automating the process of going through each element in the sequence.
#looping concept make python programming more powerful and it saves plenty of time of a programmer 

name= 'insha'
for i in name:
    print(i)

colors= ["red", "green", "blue", "black"]
for color in colors:
    print(color)             #This is simple loop but we can iterate the string also
    for i in color:
        print(i)

#Range
for x in range(6):
    print(x)      #when u use range function it starts from 0 and end before the value u enter. 

for a in range(8):
    print(a +1)              #but if we want start from 1 so we can use this:

list_1= ["ahmed", "rehman", "rizwan", "salman", "kamran"]
for x in list_1:
    print(x)        #This is mechanism of For loop.

#Break
list_2= ["ameen", "saleem", "kareem", "raheem"]
for a in list_2:
    print(a)
    if a == "kareem":
        break       #with the break statement we can stop the loop before it has looped through all the items:

list_3= ["apple", "banana", "lychee"]
for b in list_3:
    if b == "banana":
        break
    print(b)       #but this time the break comes before the print

#Continue
list_4= ["raheel", "insha", "saad"]
for Z in list_4:
    if Z == "insha":
        continue
    print(Z)      #With this we can stop the current iteration and continue from the next.

list_5= ["apple", "banana", "kiwi", "guava"]
for x in list_5:
    if x == "kiwi":
        continue
    print(x)    



class_1= ["raheel", "insha", "saad"]
for x in class_1:
    print(x)
    for i in x:
        print(i)     #Nested Loop

