a = int(input("Enter your age: "))
print("Your age is: ", a)
if(a>18):
    print("you can drive")
    print("Yes")
else:
    print("you can not drive")
    print("Yey!")
  
# ============================ Conditionals operators in python ==========================

'''
    Equals:                         a == b
    Not Equals:                     a != b
    Greater than:                   a > b
    Greater than or equal to:       a >= b
    less than:                      a < b
    less than equal:                a <= b

'''

print("a == 18",a == 18)
print("a != 18",a != 18)
print("a > 18",a > 18)
print("a >= 18",a >= 18)
print("a < 18",a < 18)
print("a <= 18",a <= 18)

'''
তার মানে conditionals operator use করে যখন আমরা কাজ করবো 
তখন আমরা boolean data type return হিসেবে পাবো 

if...else statement

if(condition):
    block of code...
 
    if(condition) এটা যদি true হয়ে তাহলে execute the block of code inside if statement. after execution return to the code out of the if...else block . 
else:
    block of code...
    if(condition) যদি flase হয় তাহলে execute the block of code inside else statement. after execution return to the code out of the if...else block . 
    
'''

applePrice = 210
budget = 200
if(applePrice<=budget):
    print("Alexa ! Add 1 kg apples to cart")
else:
    print(" Your budget is low . Sorry ! Do not add apples to the cart")

