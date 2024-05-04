'''
====================================String Slicing & Operations on String =======================================
'''

# Length of a String
# We can find the length of a string using len() function. 

fruit = "Mango"
len1 = len(fruit)
print("Mango is a ", len1, "letter word.")

# example of string slicing

names = "Sihab,Sifat"
print("names[0:5] is",names[0:5])
# for slicing we can use square brackets [x:x]
# brackets [x:x] -> [2:9] -> print হবে ২ থেকে শুরু হবে ৮ পর্যন্ত print করবে । 
print(len(names))
print("names[:6] is",names[:6])
print("names[0:-3] is",names[0:-3])
# meaning print(names[0:len(names)-3]) -> print(names[0:(11-3)]) -> print(names[0:8])
# যখনি আমরা slicing এর জন্য -value or [-x:-x] এরকম কিছু দিব তখনি python interpreter এটাকে string এর পুরো len() এর value থেকে সেটী substract করে দিবে 
# print (names[-10:-2]) is equal to print(names[len(names)-10:len(names)-2]) is equal to print(names[1:9])
# এখানে একটা খেয়াল করার বিষয় হচ্ছে যে 
# positive value এর ক্ষেত্রে [x:x] -> [0 থেকে শুরু ঃ যেই number দিব তার আগের নাম্বার পর্যন্ত ]
print("names[-10:-2] is",names[-10:-2])
print("names[len(names)-10:len(names)-2] is ",names[len(names)-10:len(names)-2])
print("names[1:9] is ", names[1:9])

# Quick Quiz
nm = "Harry"
print(len(nm))
print("nm[-4:-2] is ",nm[-4:-2])

am = "StringSlicing"
print(len(nm))
print("am[-12:-5] is ",am[-12:-5] )
