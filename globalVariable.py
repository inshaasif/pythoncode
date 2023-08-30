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

def multiply(num1, num2):
    print('Multiplication Result is:',num1 * num2)

def division(num1, num2):
    print('division Result is:',num1 / num2)



def math(operator, num1, num2 ):
    if(operator == "ADD"):
        addition(num1, num2)
    elif(operator == "SUB"):
        subtraction(num1,num2)
    elif(operator == "MUL"):
        multiply(num1, num2)
    elif(operator == "division"):
        division(num1, num2)
    else:
        print("Something wrong")



math("ADD",30,1000)
math("SUB",60,50)
math("MUL",2,10)
math("division",10,2)


