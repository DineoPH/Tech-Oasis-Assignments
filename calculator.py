#fucntion to add two numbers
def add(x,y):
    return x+y
#function to subtract two numbers
def subtract (x,y):
    return x-y
#function to multiply two numbers
def multiply(x,y):
    return x*y
#function to divide two numbers
def divide(x,y): 
    if y==0: return ("error!")
    else:
        return x/y


#Main program
print("select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#Taking input from the user
option= input("enter option(1/2/3/4):")
num1= float(input("enter first number:"))
num2= float(input("enter second number:"))

if option==1:
    print(f"{num1}+{num2} = {add(num1,num2)}") 

elif option==2:
    print(f"{num1}-{num2} = {subtract(num1,num2)}")

elif option==3:
    print(f"{num1}*{num2} = {multiply(num1,num2)}")

elif option==4:
    print(f"{num1} / {num2} = {divide(num1,num2)}")

else: print("invalid input")


