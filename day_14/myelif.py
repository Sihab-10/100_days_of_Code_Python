# suppose আমাকে একাধিক বার কিছু check করতে হচ্ছে তাহলে আমরা কি করবো । আমরা তখন elif use করবো 
# indentation is very important in python while running conditional statement 

# applePrice = 10
# budget = 200
# if(budget - applePrice > 50):
#     print("I can buy apple")
# elif(budget - applePrice > 70):
#     print(" lets ok you can buy")
# else:
#     print("I am not buying apple")

num = int(input("Enter a integer Number : "))
if(num < 0):
    print("Number is negative")
elif(num>0):
    print("Number is positive")
elif(num== 999):
    print("Number is special")
else:
    print("Number is equal to zero")
print("I am happy")
