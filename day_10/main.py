'''
================================= Taking User Input in python ==============================================
'''
'''
In python, we can take user input directly by using input() function. This input function gives a return value as string/character hence we have to pass that into a variable.

Syntax
variable = input()


But input function returns the value as string. Hence we have to typecast them whenever required to another datatype. 

'''

a = input("Enter your name: ")
print("My name is: ", a)

b = input("Enter any number: ")
print(b)
print(type(b))

# so b return value is string
#  so what we have to do  . we have to typecast the value of b

b = int(b)
print("type cast to an int value ", b)
print(type(b))
