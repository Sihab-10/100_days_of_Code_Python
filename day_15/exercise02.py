# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. 
import time
hour = int(time.strftime('%H'))
hour = int(input("Enter the hour in integer : "))
# 24 hour timing
# print("Now the time in hour is ", hour)
if(hour>=0 and hour<12):
    print("Good Morning Sir")
    print("Eat Your Breakfast")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
    print("Eat Your lunch")
elif(hour>=17 and hour<=24):
    print("Good night Sir")
    print("Eat your Dinner")
else:
    print("Buy")


