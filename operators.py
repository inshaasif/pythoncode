# #Arithmetic
# x=25
# y=32
# print(x+y)        #addition

# a=124
# b=230
# c=280
# print(a+b+c)    #addition

# x=23
# y=12
# print(x-y)     #subtraction

# a=22
# b+12
# c=4
# print(a*b*c)    #multiplication

# u=22
# v=5
# print(u/v)     #Divison

# #Assignment
# X=25     #=
# print(x)

# x=34
# print(x+20)

# y=104
# print(y-22)

# a=23
# print(a*2)

# b=67
# print(b/2)


# #Comparison
# a=99
# b=92
# print(a==b)     #equal

# x=23
# y=12
# print(x!=y)    #NotEqual

# first_name = "insha"
# # last_name = ""

# R=253
# L=123
# print(R>L)    #Greater

# i=22
# a=23
# print(i<a)    #Lessthan

# m=122
# n=193
# print(m>=n)   #GreaterEqualTO

# o=23
# p=222
# print(o<=p)    #LessEqualTo

# #Logical
# Z=12
# print(Z>3 and Z<50)    #and

# y=22
# print(y>12 or y<20)     #OR

# p=235
# print(not(p>222 and p<322))   #NOT

#  Gobal variable

company_name = "Insha"

def company():
    global company_name
    company_name = "abc"
    print("Company name ",company_name)


company_name = "Saad"

print("this", company_name)

company()

def addition(num1 , num2):
    print('Addition Result is: ',num1 + num2)


def subtraction(num1, num2):
    print('Subtraction Result is: ',num1 - num2)


def math(operator, num1, num2 ):
    if(operator == "ADD"):
        addition(num1, num2)
    elif(operator == "SUB"):
        subtraction(num1,num2)
    else:
        print("Something wrong")


addition(10,20)

subtraction(60,50)

math("ADDD",30,1000)





