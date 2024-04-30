'''
    ----------------------------- Typecasting in python -------------------

    The conversion of one data type into the other data type is known as type casting in python or type conversion in python. 

    Python supports a wide variety of functions or methods like:
    int(),float(),str(),ord(), hex(), oct(), tuple(), set(), list(), dict(), etc fot the type casting in python.


    Two types of Typecsting:
    1. Explicit Coversion (Explicit type casting in python )
    আমি ইচ্ছা করে type casting করতেসি । 
    2. Implicit Conversion (Implicit type casting in python)
    python নিজে automatic typecasting করতেসে ।
    
    Data types in python do not have the same level i.e. ordering of data types is not the same in python . Some of the data types have higher order . whil e performing any operations on variables with different data types in python, one of the variables data types will be changed to the higher data type. 
    According to the level, one data type is converted into other by the python interpreter itself (automatically). This is called, implicit typecasting in python. 
    
    Python converts a smaller data type to a higher data type to prevent data loss. 

'''

a = "1"
# a = 1
b = "2"
# b = 2
print(int(a)+int(b))

# Example of explicit typecasting
string = "15"
number = 4
string_number = int(string)
sum = number + string_number
print("The sum of both the number is : ", sum)

#Example of implicit typecasting

c = 1.9 # flot (higher order data type)
print("Here c is: ", type(c))
d = 8 # int (lower data type)
print("Here d is: ",type(d))
e = c+d
print("The sum of e = c + d is: ", e); # float (higher order data type) (automatically convert python)
print("Here e is: ", type(e))
