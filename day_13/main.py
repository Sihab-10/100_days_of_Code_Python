'''
================================ String Methods in Python ==============================
'''

# String Method
'''
Python provides a set of built in methods that we can use to after and modify the strings. 
'''
'''
Strings are immutable . it can not be changed. 
'''

# Upper():

'''
The upper() method converts a string to upper case . convert the existing string to a new string.
'''
# for emaple
str1 = "AbcDefghIj"
print(str1.upper())

# lower()

'''
The lower() method converts a string to lower case. convert the existing string to a new string.
'''
# for example
str2 = "ABEghIJ"
print(str2.lower())


# strip()

'''
The strip() method removes any white spaces before and after the string. 
'''

str3 = "   Blue Moon   "
print(str3.strip())

# rstrip()

'''
the rstrip() removes any trailing characters. Example:
'''
str4 = "Hello!!!!!"
print(str4.rstrip("!"))


# replace()

'''
The replace() method replaces all occurences of a string with another string. 
'''

str5 = "Silver Moon"
print(str5.replace("M", "Sp"))


# split()

'''
The split() method splits the given string at the specified instance and returns the sparated strings as list items. 
'''

str6 = "Golden Egg with a Golden Chicken"
print(str6.split(" ")) # split the string at the whitespace " "

# capitalize()

'''
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase
'''

blogHeading = "introduction to JS"
print(blogHeading.capitalize())


# center()

'''
The center() method aligns the string to the center as per the parameters given by the user
'''
str7 = "Welcome to the Console!!!"
print(str7.center(50))
print("Length of str7 is :",len(str7))
print("Lengthe of str7 after using str7.center(50) is :",len(str7.center(50)))

# We can also provide padding character. It will fill the rest of the fill character by the user. 

# Example

str71 = "Welcome to the Console!!!"
print(str71.center(50, ".")) 

# count()

'''
The count() mehtod returns the number of times the given value has occured within the given string. 
'''

str8 = "Abracadabra"
countStr = str8.count("a")
print(countStr)


# endswith()

'''
The endswith() method checks if the string ends with a given value. If yes then return True, else return false
'''

str9 = "Welcome to the console !!!"
print(str9.endswith("console !!!"))

# another example

str10 = "Welcome to the console !!!"
print(str10.endswith("to", 4, 10))

# find()

'''
The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1
'''

str11 = "He's name is Dan. He is an honest man."
print(str11.find("is"))

# index()

'''
The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception. 
'''
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

'''
As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
'''

#isalnum()

'''
The isalnum() method returns True only if the entire string only consists of
alphanumeric : A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
'''

str12 = "Welcome"
print(str12.isalnum())


# isalpha()

'''
The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
'''

str13 = "Hello world"
print(str13.isalpha())

# islower()

'''
The islower() method returns True if all the characters in the string are lower case, else it returns False.
'''

str14 = "123abc"
print(str14.islower())


# isprintable() :

'''
The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
'''

str15 = "We wish you a Happy Eid\n"
print(str15.isprintable())


# isspace() 

'''
The isspace() method returns True only and only if the string contains white spaces, else returns False.
'''

str16 = "       "
print(str16.isspace())

# title()

'''
The title() method capitalizes each letter of the word within the string.
'''

str22 = "He's name is Dan. Dan is an honest man."
print(str22.title())

# istitle()

'''The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False
'''

str17 = "Hello This Is Sihab"
print(str17.istitle())
str18 = "Hello this is sihab"
print(str18.istitle())

# isupper() :

'''
The isupper() method returns True if all the characters in the string are upper case, else it returns False.
'''

str19 = "WORLD HEALTH ORGANIZATION" 
print(str19.isupper())

# startswith() :

'''
The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
'''
str20 = "Python is a Interpreted Language" 
print(str20.startswith("Python"))

# swapcase() :

'''
The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
'''

str21 = "Python is a Interpreted Language" 
print(str21.swapcase())