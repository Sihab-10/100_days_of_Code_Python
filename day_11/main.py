'''
================================== Strings in Python ====================================================
'''

'''
What are strings?
In python, anything that you enclose between signle or double quotation marks is considered a string. A string is essentially a sequence or array of texual data. Strings are used when working with Unicode characters. 
'''

name = "Siahb";
friend = 'Sifat'
print(name);
print(friend);

# string concatenation

print("Hello , " + name);

'''
Note: It does not matter whether you enclose your stings in single or double quotes, the output remains the same.
Sometimes, the user might need to put quotation marks in between the strings. 
example, consider the sentence: He said, "I want to eat an apple". 
We will definitely use single quotes for our convenience. 
'''

print('He said, "I want to eat an apple."');

'''
Multiline Strings
If our string has multiline lines, we can create them like this:
'''
print("Multiline comments ....................")
a = """Hello, Sihab 
How are you?
I am fine, thank you. How about you?
Great to see you"""
print(a);

'''
String is a sequence of character in programming language, meaning its indexing starts with 0 to the next number 1 2 3 ....

S   i   h   a   b
0   1   2   3   4
'''

string1 = "something";
print(string1[0])
print(string1[1])
print(string1[2])
print(string1[3])
print(string1[4])
print(string1[5])
print(string1[6])
print(string1[7])
print(string1[8])
#print(string1[9]) this throw an error.

# আমরা চাচ্ছি যে এগুলো একবারে print করতে তাহলে কি কোনো উপায় আছে python এ । yes একটা উপায় আছে সেটা হলো ঃ
print("let use a for loop to print it at once")
for character in string1:
    print(character);

for character in a:
    print(a);
