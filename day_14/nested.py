num = int(input("Enter an integer number between 11 to 20: "))
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1 to 10")
    elif(num > 10 and num <= 20):
        print("Number is between 11 to 20")
    else:
        print("Number is greter than 20")
else:
    print("Number is 0")