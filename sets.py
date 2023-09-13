#Points
#Sets are used to store multiple data into single variable.
#Sets are unordered, unchangeable and unindexed.
#we can add or remove items in sets.
#Sets are written in curly brackets.
#Duplicates will be ignored in sets.

example_1= {"apple", "banana", "cherry"}
print(example_1)   #Sets

example_2= {"saad", "insha", "ali", "saad", "raheel"}
print(example_2)    #Duplicates will be ignored

example_3= {True, 1, "anas", "amsal"}
print(example_3)    #Duplicates

example_4= {"saad", "insha", "ali", "raheel"}
print(len(example_4))  #Length

example_5= {"monday", "tuesday", "wednesday"}
example_6= {1, 5, 8, 9}
example_7= {True, False, True}

print(example_5)
print(example_6)
print(example_7)   #Any Data Type

example_8= {"abc", "def", "geh"}
print(type(example_8))    #Type()

example_9= set(("python", "java", "C++"))
print(example_9)    #Constructor()
#Note constructor will use round brackets only.