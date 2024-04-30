'''
-------------------------Comments, Escape Sequences & Print Statement-----------------------------

'''

print("I am a good boy")
print("hello")
print("How are you")
print("I am fine thank you")
# to print anything in new line use \n 
print("How 's your day going \nI am a good boy")

''' ------------------------------------ Comment----------------------------------------'''
'''what is comment'''
# comment is something that is not execute in the code
'''Single line Comment'''
# this is a signle line comment . 
'''Mulitline comment'''
# To write mulit-line comments you can use '#' at each line or you can use the multiline string
'''
this is multiline comment 
'''

"""
This is also a multiline comment
"""

"""This is an if-else statement. 
It will execute a block of code if a specified condition is true. 
If the condition is false then it will execute another block of code."""

p=7
if (p>5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

'''----------------------------------Escape Sequence Characters -------------------------'''
"""
To insert characters that cannot be directly used in a string, we use an escape sequence character.
An escape sequence character is a backslash \ followed by the character you want to insert.


"""
# print("This doesn't "execute")
print("This will \" execute")
print("This is a \" $ symbol \" and the $ symbol is used in an american currency")
print("Hey", 8, 7, sep="~", end="008\n")
# sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
# end='end': Specify what to print at the end. Default is '\n' (line feed)
# file: An object with a write method. Default is sys.stdout
print("Harry")





