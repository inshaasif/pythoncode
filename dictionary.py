#Points.
#Dictionary are used to store data value in key:value pairs.
#dictionary is ordered, changeable and do not allow duplicates.
#Dictionary are written in curly bracket and have key and values.
#Dictionary can be of any data types.

Thisdict= {
    "brand": "Dell" ,
    "model": "corei5" ,
    "year": "2015"
}
print(Thisdict)    #Dictionary 

example_1= {
    "brand": "Toyota" ,
    "model": "Corolla" ,
    "Year": "2020"
    }
print(example_1["brand"])  #Dictionary Items

example_2= {
    "class": "Python" ,
    "timing": "8am" ,
    "students": "3" ,
    "students": "2"
}
print(example_2)   #Duplicates not allowed 

example_3= {
    "class1": "Python" ,
    "class2": "Java" ,
    "class3": "C++"
}
print(len(example_3))    #Length ()by using round brackets

example_4= {
    "string": "Ford" ,
    "Boolean": True ,
    "Integer": 22 ,
    "colors": ["red", "blue", "white"]
}
print(example_4)    #Dictionary can be any type

example_5= {
    "class1": "Python" ,
    "class2": "Java" ,
    "class3": "C++"
}
print(type(example_5))   #Dictionary Type

example_6= dict(Country= "Pakistan", Independenceday= "14aug", name= "Insha")
print(example_6)    #Dictionary Constructor()