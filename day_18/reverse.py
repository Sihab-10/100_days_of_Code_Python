count = 5
while(count>0):
    print(count)
    count=count-1;
else:
    print("I am inside else")


# do{
#     # loop body
# }while(condition)

# how to emulate do while loop in python?

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break