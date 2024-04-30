'''-----------------------------------Variables and Data types in Python ------------------------------'''
'''
What is variable?
Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar,salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing. 

'''
a = 1
b = True
c = "Harry"
d = None
# These are four variables with different types

# What is Data Type?
'''যখন কোন একটা variable এর মধ্যে কি ধরনের বা type এর data store হচ্ছে তাকে বলা হয় data type '''
'''Data type specifies the type of value a variable holds . This is required in programming to do various operations without causing an error'''
# In python we can print the type of any operator using type function:

# By Default python provides the following built in data types:
'''
1. Numeric data: int, float, complex

-> int: 3, -8, 0
-> float: 7.349, -9.0, 0.000001
-> complex: 6+2i

2. Text data: str

str:"Hello world", "Python Programming"

3. Boolean data:
Boolean data consits of values True or False.

4. Sequence data: list, tuple

list: list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation. 

Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed withing a parentheses. Tuples are immutable and can not be modified after creation. 

5. Mapped data: dict

dict: A dictionary is an unordered collection of data containing a key:value pair. 

The key:value pairs are enclosed withing curley brackets.

'''
# numeric
a = 1
print(type(a))
b = 1.1
print(type(b))
a = complex(8,2)
print(a)
print(type(a))

# list

list1 = [8, 2.3, [-4,5], ["apple", "banana"] ]
print(list1)

# tuple
tuple1 =(("parrot", "sparrow"), ("lion", "tiger"))
print(tuple1)

#dict

dict1={"name":"Sihab", 
       "age":20,
       "canVote": True}
print(dict1)

'''***Python all variables are work like an object'''
'''পাইথন সবকিছু একটা অবজেক্ট এর মত কাজ করে '''