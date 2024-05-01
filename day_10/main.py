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

# A basic arithmatic operation by two integers

x = input("Enter any number :")
y = input("Enter another number : ")

print("The addition of these two number is : ",int(x)+int(y))

# যখনি python এর সাহায্যে কোন input নিব তখন অবশ্যই সেটার return হিসেবে যখন কোন কিছু আনবো (সেটা হতে পারে int, float etc) তখন return value হিসেবে যেই data type আনতে চাচ্ছি সেটাতে typecast করে নিব । 
 
print("This is a calculator, Use it for fun.. 😊")
i = input("Enter your number : ")
j = input("Enter another number : ")
k = print("The addition of two number is : ", float(i) + float(j))
k = print("The Substraction of two number is : ", float(i) - float(j))
k = print("The Multiplication of two number is : ", float(i) * float(j))
k = print("The Division of two number is : ", float(i) / float(j))
k = print("The floor Division of two number is : ", float(i) // float(j))
