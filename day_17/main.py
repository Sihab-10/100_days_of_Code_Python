'''
=========================== loops in python =============================

'''

'''
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops.Based on this loops are further classified into following types; for loop, while loop, nested loops. 

'''

'''
for loop 

for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

'''
# Example : iterating over a string
name = "SihabSarar"
for i in name :
    print(i, end=", ")
    if(i =="b"):
        print("This is something special!")

#Example : iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i) 

# range():

'''
What if we do not want to iterate over a sequence ?
What if we want to use for loop for a specific number of times?

here, we can use the range() function. 
'''
# loop যদি specefic বার করতে হয় তাহলে আমরা সেটা করতে পারি range function এর মাধ্যমে 
# example: 0 to 5 print করতে হলে আমরা just use করবো এভাবে 
for k in range(5):
    print(k)
# example: যদি 1 to 5 print করতে চাই তাহলে এভাবে 
for k in range(5):
    print(k + 1)
# example: যদি 1 to 8 print করতে চাই তাহলে এভাবে 
for k in range (1, 9):
    print (k)
# example: যদি 1 to 2000 print করতে চাই তাহলে এভাবে 
for k in range(1, 2001):
    print(k)
# example: যদি n সংখ্যক number বাড়ায় কিছু করতে হয় তাহলে এভাবে করবো 
for k in range(1, 10, 3):
    print(k)