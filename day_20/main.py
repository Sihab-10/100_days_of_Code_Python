'''
========================================= Functions in python ==============================
'''

'''ধরেন আপনি একটা block of code কে  আপনার program এ ১০ অথবা ৫০ বার use করতেসেন তাহলে কি আপনি সেটাকে বার বার copy and paste করবেন এটা জেনেও যে সেই block of code টা ১০ থেক ২০ হাজার লাইন এর । না , আপনি সেটা করবেন না । আপনি কি করবেন সেই block of code কে একটা function এর মধ্যে দিয়ে দিবেন এবং তাকে প্রয়োজন অনুসারে call করে করে নিজের মত করে use করবেন । এটাই হলো function এর সুবিধা। '''

'''
Python functions

A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we haver large amounts of code, it is advisable to create or use existing functions taht make the program flow organized and neat. 

There are two types of functions:

1. Built in funciton 
2. User defined funcitons 

# Built in function 

These funcitons are defined and pre-coded in python . Some examples of built in funcitons are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print() etc

# User define function 

We can create funcitons to perform specific tasks as per our needs. Such functions are called user defined functions. 

'''

# syntax of a function in python
'''# def function_name(argument,argument,...):
        operation or logics with declared argument

then use this function in any where with this syntax
    function_name(variable, variable)
    
    '''
def name(fname, lname):
    print("hello", fname, lname)

name("Sihab", "Sarar")
name("Sifat", "Sarar")
name("Kaifiya", "Suha")

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
def isLesser(a, b):
    pass
# একটা function define করে যদি তার ভিতরে কি করবো সেটা যদি plan করতে থাকি বা পড়ে করবো এরকম মনে হয় তাহলে সেখানে আমরা pass keywork লিখে দিতে পারি। 
a = 9
b = 8
# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a, b)
isGreater(a, b)

c = 10
d = 50
# if(c>d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d)
isGreater(c, d)

 