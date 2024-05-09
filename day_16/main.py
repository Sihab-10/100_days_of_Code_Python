'''
======================================== Match Case Statements ====================================

'''

# Match Case Statements 

'''
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java Like Language, you must have heard of switch-case statements. If this is your first language, dont worry as I will tell you everything you need to know about match case statements in this video!
'''

# A match statement will compare a given variable's value to different shapes, also referred to as the pattern. the main idea is to keep on comparing the variabel with all the present patterns until it fits into one. 

# The match case consists of three main entities:
'''
1. The match keyword
2. One or more case clauses
3. Expression for each case

'''

# The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches. 

x = int(input("Enter a number in between 0 to 4: "))
# x is the variable to match 
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if condition 
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # empty case with if condition 
    case _ if x<10:
        print("x is < 10")

    case _ if x!=80:
        print(x, "is not equal 50")
    
    case _ if x!=90:
        print(x, "is not equal 90")
    # defult case(will only be matched if the above cases were not matched)
    #so it is    basically just an else
    case _:
        print(x)

'''
python এ আমরা break use করি  না । প্রথম যার সাথে match হবে সেটা print হয়ে berak হবে  । 
'''