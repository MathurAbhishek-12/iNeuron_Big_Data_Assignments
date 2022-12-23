#!/usr/bin/env python
# coding: utf-8

# Q1. Why do we call Python as a general purpose and high-level programming language?

# Python's interpreter acts as an interface to convert high level programming language to low level language that is easily understandable by computer (i.e. 0 & 1). That's why it is called as general purpose and high-level programming language.

# Q2. Why is Python called a dynamically typed language?

# Dynamic typing means that variable type is determined only while running the code. That's why Python is called a dynamically typed language.

# Q3. List some pros and cons of Python programming language?

# PROS: It is a dynamic language, can run different programs through this, acts as an interpreter for converting high level language to low level language, 
# 
# CONS: It takes time to become professional in understanding code, for visualization: Python interface is not interactive as other tools like Tableau, PowerBI.

# Q4. In what all domains can we use Python?

# Software engineers, Data Scientists, Data Engineering, Game Developers, etc.

# Q5. What are variable and how can we declare them?

# Variables are the keywords that we define for particular data type. WE declare them by assigning any value to them. For eg: a=4, b=4.0, c = "Hi"; where a is integer, b is float, c is string

# Q6. How can we take an input from the user in Python?

# By using input() in code. For eg:
# inp = input('STATEMENT')

# Q7. What is the default datatype of the value that has been taken as an input using input() function?

# String

# Q8. What is type casting?

# Type Casting is a method to convert a datatype into another. eg: int() to float()
# Two Types: Implicit TypeCasting: Done automatically. eg: a=2.2 --> a is automatically set as float
#            Explicit TypeCasting: Done manually. eg: int("Abhi") --> converting string to int

# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

# We can't take more than one input from the user using single input() function. If we want more than 1, then we need to put split() function. 
# eg: x,y=input("Enter 2 no's").split()
#     print(x,y)

# Q10. What are keywords?

# Keywords are predefined and reserved words in python that have special meanings. The keyword cannot be used as an identifier, function, and variable name. All the keywords in python are written in lower case except True and False.
# 
# Eg: and, or, not, if, elif, etc.

# Q11. Can we use keywords as a variable? Support your answer with reason.

# No because keywords are reserved words. 
# eg: True = "Abhi"
# The above code is not valid as True is reserved.

# Q12. What is indentation? What's the use of indentaion in Python?

# Indentation is the space before the code. For eg: after every function or for loop, there is a predefined space to put; that space is used to clearly show the alignment of the code as well as help the interpreter to understand that what part of the code belongs to what part.

# Q13. How can we throw some output in Python?

# By using print() command or if we write direct variable, it will also deliver the output but only once.

# Q14. What are operators in Python?

# Operators are used to perform some calculation in a code. For eg: +,-,/,//,%,**,etc.

# Q15. What is difference between / and // operators?

# / means division in float and // means division in int.
# 
# For eg: 4/2 = 2.0 and 4//2 = 2

# Q16. Write a code that gives following as an output.
# ```
# iNeuroniNeuroniNeuroniNeuron
# ```

# In[ ]:


print("iNeuron"*4)


# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

# In[ ]:


a = int(input("Enter a number"))
if(a%2==0):
    print("even")
else:
    print("odd")


# Q18. What are boolean operator?

# The logical operators and, or and not are also referred to as boolean operators. They helps in checking the condition of a code.

# 
# Q19. What will the output of the following?
# ```
# 1 or 0
# 
# 0 and 0
# 
# True and False and True
# 
# 1 or 0 or 0

# 1
# 0
# False
# 1

# Q20. What are conditional statements in Python?

# Python has 3 key Conditional Statements: if statement; if-else statement; if-elif-else 

# Q21. What is use of 'if', 'elif' and 'else' keywords?

# If we want to filter out a condition from a list, then 'if' statement can be used.
# If there are multiple filters that we need to check, then with 'if', 'elif' and 'else' statement is used.

# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

# In[ ]:


b = int(input("Enter your age"))
if(b >= 18):
    print("I can vote")
else:
    print("I can't vote")


# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```

# In[ ]:


def my_function(number):
    sum = 0
    for i in number:        
        if(i%2 == 0):
            sum = sum + i            
    return(sum)
    
numbers = [12, 75, 150, 180, 145, 525, 50]
c = my_function(numbers)
print(c)


# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

# In[ ]:


x,y,z = input("Enter 3 no's").split()
print(max(x,y,z))


# Q25. Write a program to display only those numbers from a list that satisfy the following conditions
# 
# - The number must be divisible by five
# 
# - If the number is greater than 150, then skip it and move to the next number
# 
# - If the number is greater than 500, then stop the loop
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```

# In[ ]:


def my_function(number):
    for i in number:
        if(i%5==0):
            if(i>150):
                continue
            elif(i>500):
                break
            print(i)
                

numbers = [12, 75, 150, 180, 145, 525, 50]
my_function(numbers)


# Q26. What is a string? How can we declare string in Python?

# A string is a variable that stores a character or a long word or paragraph. For eg: a = "Hi" or b = str(7)

# Q27. How can we access the string using its index?

# In[ ]:


For eg:
a="Hi there!"
a[0]           # It will show the value at first index i.e. "H"


# Q28. Write a code to get the desired output of the following
# 
# string = "Big Data iNeuron"
# desired_output = "iNeuron"

# In[ ]:


string = "Big Data iNeuron"
print(string[9:16])

OR

string = "Big Data iNeuron"
string[-7::1]                  # step value remains 1 by default

OR

string = "Big Data iNeuron"
string[-7::]


# Q29. Write a code to get the desired output of the following
# 
# string = "Big Data iNeuron"
# desired_output = "norueNi"

# In[ ]:


string = "Big Data iNeuron"
print(string[-1:7:-1])


# Q30. Resverse the string given in the above question.

# In[ ]:


string = "Big Data iNeuron"
print(string[-1::-1])


# Q31. How can you delete entire string at once?

# In[ ]:


string = "Big Data iNeuron"
del string


# Q32. What is escape sequence?

# In[ ]:


Character combinations consisting of a backslash (\) followed by a letter or by a combination of digits are called "escape sequences."

For eg:
\n (New Line) It is used to create a new line.
\t (Tab).
\' (Printing single quotation)
\” (printing double quotation)


# Q33. How can you print the below string?
# 
# 'iNeuron's Big Data Course'

# In[ ]:


print("iNeuron's Big Data Course")


# Q34. What is a list in Python?

# In[ ]:


Lists are used to store multiple items in a single variable. 
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary.


# Q35. How can you create a list in Python?

# In[ ]:


my_list = [1,2,3,[1,2,9],"Any string"]


# Q36. How can we access the elements in a list?

# In[ ]:


my_list = [1,2,3,[1,2,9],"Any string"]
my_list[0]  # In bracket, write index number and it will display the item at that number.


# Q37. Write a code to access the word "iNeuron" from the given list.
# 
# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]

# In[ ]:


lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
lst[4][2]


# Q38. Take a list as an input from the user and find the length of the list.

# In[ ]:


my_list = [] 

for items in range(1000):
    a = input(f"Enter item; type: \"close\" if you want to end this list")
    if(a=="close"):
        break
    else:
        my_list.append(a)
    
print(f"lenght of the list is:{len(my_list)}")


# Q39. Add the word "Big" in the 3rd index of the given list.
# lst = ["Welcome", "to", "Data", "course"]

# In[ ]:


lst = ["Welcome", "to", "Data", "course"]
lst.insert(2,"Big")


# Q40. What is a tuple? How is it different from list?

# Tuple is a data type in python out of 4 datatypes i.e. list, tuple, dictionary and Set. Tuple is used to store multiple items of data. Whatever is typed in a tuple cannot be altered or modified after execution of the code. That's why a tuple is immutable and a list is mutable.

# Q41. How can you create a tuple in Python?

# A tuple can be created by putting all the items in a parentheses().

# Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

# In[ ]:


t = (1,2,"Rahul")
t.append("Abhi")

No, I 'm not able to add any value because tuple doesn't support modification or update in it's items.


# Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

# In[ ]:


t = (1,2,"Rahul")
t2 = (3,4,"Abhi")
t.append(t2)

As tuple has no attribute "append"; therefore it can't be appended.


# Q44. Take a tuple as an input and print the count of elements in it.

# In[ ]:


t = (1,2,"Rahul")
print(len(t))        # 3


# Q45. What are sets in Python?

# Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable, and unindexed.

# Q46. How can you create a set?

# In[ ]:


eg: set3 = {1,2,3,4,5,2,1,4}
    print(s3)                   # output: {1, 2, 3, 4, 5}


# Q47. Create a set and add "iNeuron" in your set.

# In[ ]:


set3 = {1,2,3,4,5,2,1,4}
set3.append("iNeuron")

Error: 'set' object has no attribute 'append'


# Q48. Try to add multiple values using add() function.

# In[ ]:


a = [1,2,3]
a.add(4)
a             # o/p: Error: 'list' object has no attribute 'add'  

set3 = {1,2,3,4,5,2,1,4}
set3.add("iNeuron")
set3                 # o/p: {1, 2, 3, 4, 5, 'iNeuron'}


# Q49. How is update() different from add()?

# In[ ]:


add() takes exactly one argument while update() can add multiple at once

For eg:
set3 = {1,2,3,4,5,2,1,4}
set3.update(["iNeuron",7,5])
set3                          # o/p: {1, 2, 3, 4, 5, 7, 'iNeuron'}


# Q50. What is clear() in sets?

# In[ ]:


The clear() method removes all elements in a set.
eg: 

set3 = {1,2,3,4,5,2,1,4}
set3.update(["iNeuron",7,5])
set3.clear()
set3                   # o/p: set()


# Q51. What is frozen set?

# frozenset() method/function creates an immutable (uncahngeable) Set 

# Q52. How is frozen set different from set?

# "Frozenset" is similar to "Set" in Python, except that frozensets are immutable (unchangeable), which implies that once generated, elements from the frozenset cannot be added or removed

# Q53. What is union() in sets? Explain via code.

# In[ ]:


Union in sets combine sets and merge them through a common attribute. It doesn't show the duplicate values.

For eg: 
set1 = {1,2,3}
set3 = {1,2,3,4,5,2,1,4}
print(set1 | set3)        # o/p: {1, 2, 3, 4, 5}


# Q54. What is intersection() in sets? Explain via code.

# In[ ]:


Intersection in sets displays only the common in sets. It doesn't show the duplicate values.

For eg:
set1 = {1,2,3}
set3 = {1,2,3,4,5,2,1,4}
print(set1 & set3)        # o/p: {1, 2, 3}


# Q55. What is dictionary in Python?

# Dictionary in Python is used to store key:value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates.

# Q56. How is dictionary different from all other data structures.

# Dictionary is a default python data structure used to store the data collection in the form of key-value pairs. Dictionaries are written inside the curly brackets ({}), separated by commas.
# 
# * Dictionary is ordered, mutable but do not allow dulpicated with same key. eg: dict={"A":"X","B":"Y","A":"Z"} ; As here are two values with same key "A", so it will show only one in o/p which is updated at last i.e. "A":"Z"
# 
# * List is ordered, mutable and allow duplicates. eg: list=[1,2,1]
# 
# * A set is a collection which is unordered, unchangeable, allow duplicates and unindexed. eg: set = {1,2,3,4,5,2,1,4}
# 
# * A tuple is ordered, immutable, allows duplicates. eg: t = (1,2,"Rahul",1)

# Q57. How can we declare a dictionary in Python?

# In[ ]:


sample_dict = {
  "vegetable": "potato",
  "fruit": "banana",
  "chocolate": "gems"
}
print(sample_dict)


# Q58. What will the output of the following?
# 
# var = {}
# print(type(var))

# In[ ]:


class 'dict


# Q59. How can we add an element in a dictionary?

# In[ ]:


dict.update({'key3': 'name'})

OR

dict1 = {'key4': 'is', 'key5': 'fabulous'}
dict.update(dict1)


# Q60. Create a dictionary and access all the values in that dictionary.

# In[ ]:


sample_dict = {
  "vegetable": "potato",
  "fruit": "banana",
  "chocolate": "gems"
}
print(sample_dict)


# Q61. Create a nested dictionary and access all the element in the inner dictionary.

# In[ ]:


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
people[1]


# Q62. What is the use of get() function?

# In[ ]:


The get() method returns the value of the item with that key.

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
people.get(1)  


# Q63. What is the use of items() function?

# In[ ]:


In Dictionary, items() method is used to return the list with all dictionary keys and values.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)                # o/p: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# Q64. What is the use of pop() function?

# In[ ]:


The pop() method removes the specified item from the dictionary.

eg: car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)               o/p: {'brand': 'Ford', 'year': 1964}


# Q65. What is the use of popitems() function?

# In[ ]:


The popitem() method removes the item that was last inserted into the dictionary.

eg: car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
car.popitem()
print(car)            o/p: {'brand': 'Ford', 'model': 'Mustang'}


# Q66. What is the use of keys() function?

# In[ ]:


Display all the key value in a dictionary.

eg: car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)               o/p: dict_keys(['brand', 'model', 'year'])


# Q67. What is the use of values() function?

# In[ ]:


Display all the values in a dictionary.

eg: car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
car["year"] = 2018
print(x)                 o/p: dict_values(['Ford', 'Mustang', 2018])


# Q68. What are loops in Python?

# Loops means repeating a code until any condition is met.

# Q69. How many type of loop are there in Python?

# 3 types: For, while and nested loop

# Q70. What is the difference between for and while loops?

# In for loop, range is given and it increments automatically whereas in while loop, we have to put manual increment at the end of the loop to keep it repeating till the condition is met.

# Q71. What is the use of continue statement?

# When the continue statement is executed in a loop, the code inside the loop that comes after the continue statement will be skipped for the current iteration and the next iteration of the loop will start. This makes the continue statement in Python a loop control statement that forces to execute the next iteration of the loop while skipping the rest of the code inside the loop for the current iteration only.
# 
# eg:
# 
# for var in "Abh":
#     if var == "b":
#         continue
#     print(var)              #o/p: A
#                                   h

# Q72. What is the use of break statement?

# Break statement terminate the loop. It is used to bring the control out of the loop when some external condition is met. If the break statement is inside a nested loop, the break will terminate the innermost loop.
# 
# eg:
# 
# for i in range(10):
#     print(i)
#     if i == 2:
#         break

# Q73. What is the use of pass statement?

# The pass statement is used as a placeholder for future code.
# 
# When the pass statement is executed, nothing happens, but you avoid getting an error
# 
# a = 33
# b = 200
# if b > a:
#   pass
# 
# #having an empty if statement like this, would raise an error without the pass statement

# Q74. What is the use of range() function?

# range() function is used to define range in a for loop; i.e. till where the loop is iterable.

# Q75. How can you loop over a dictionary?

# In[ ]:


my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for g,m in my_dict.items():
    if (g=='year'):
        print(g,m)


# Coding problems
# Q76. Write a Python program to find the factorial of a given number.

# In[ ]:


a = int(input("Enter a no"))
m=1
for i in range(a):
    b=i+1
    m=b*m
print(f"The factorial of the given number is: {m}")


# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100

# In[ ]:


P = int(input("Enter a P no"))
R = int(input("Enter a R no"))
T = int(input("Enter Time"))

SI = (P*R*T)/100
print(SI)


# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

# In[ ]:


def amar(P,R,T):
    A = (P*pow((1+ R/100),t))
    print(A)

P = float(input("Enter a P no"))
R = float(input("Enter a R no"))
T = float(input("Enter Time"))
amar(P, R,T)


# Q79. Write a Python program to check if a number is prime or not.

# In[ ]:


def prime_check(a):
    for i in range (2,a+1):
        if(i==a):
            continue
        elif(a%i==0):
            print("This is not a prime number")
            return("not prime")
            quit()
            

a = int(input("Enter a no to check for prime"))

if(a==0):
    print("0 is neither prime nor composite")
    end()
    
r = prime_check(a)

if(r == None):
    print("This is a prime number")


# Q80. Write a Python program to check Armstrong Number.

# In[ ]:


a = input("Enter a no. to check for armstrong")  # a is a string
l = len(a)                                       # l is int
b=0
for var in a:                                    # var is string
    b = (int(var))**l + b                        # converted var to integer type bcz string can't perform calculation. 
    
print(b)


# Q81. Write a Python program to find the n-th Fibonacci Number.

# In[ ]:


n = int(input("Enter a no to find nth fibonacci number"))

a=0
b=1

if(n==1):
    print('0')

    
elif(n==2):
    print('1')

for i in range(n-2):
    c=a+b
    a=b
    b=c
        
if(n>2):
    print(c)  


# Q82. Write a Python program to interchange the first and last element in a list.

# In[ ]:


lst = [1,2,3,4,5,6]
a = len(lst)

b = lst[a-1]
lst[a-1] = lst[0]
lst[0] = b

print(lst)


# Q83. Write a Python program to swap two elements in a list.

# In[ ]:


lst = [1,2,3,4,5,6]
pos1 = int(input("Enter pos 1 to swap"))
pos2 = int(input("Enter pos 2 to swap"))

b = lst[pos1]
lst[pos1] = lst[pos2]
lst[pos2] = b

print(lst)


# Q84. Write a Python program to find N largest element from a list.

# In[ ]:


lst = [1,10,10,68, 2,3,15,4,5,6]
n = int(input("Enter N largest elements that you want to see"))
empty_lst = []

for i in range(n):
    m=0  
    
    for j in range(len(lst)):
        if (lst[j]>m):
            m=lst[j]
                
    lst.remove(m)
    empty_lst.append(m)
    
print(empty_lst)


# Q85. Write a Python program to find cumulative sum of a list.

# In[ ]:


def cumulative_sum(lyst):
    av=0
    for i in range(len(lyst)):
        av = lyst[i]+av
    print(av)

lyst = []
n = int(input("Enter no. of values for list"))
for i in range(n):
    e = int(input("Enter value"))
    lyst.append(e)
print(lyst)    

cumulative_sum(lyst)


# Q86. Write a Python program to check if a string is palindrome or not.

# In[ ]:


a = input("Enter a string")

if(a==a[::-1]):                      # when we do a[::-1] , it starts from the end, towards the first.
    print("pallindrome")
else:
    print("Not a pallindrome")


# Q87. Write a Python program to remove i'th element from a string.

# In[ ]:


a = input("Enter a string")
i = int(input("Enter ith element to remove from this string"))
new_str = ''

for j in range (len(a)):
    if(j!=i):
        new_str = new_str + a[j]

print(new_str)


# Q88. Write a Python program to check if a substring is present in a given string.

# In[ ]:


a = input("Enter a string").lower()
b = input("Enter a string to find in previous string").lower()

if b in a:
    print("Yes present")
else:
    print("not present")


# Q89. Write a Python program to find words which are greater than given length k.

# In[ ]:


a = input("Enter a string").lower()
k = int(input("Enter length of words"))
my_str=[]

text = a.split(" ")  # split() will split the string where space is present(eg: ["Hi my name is"]-->["Hi","my","name","is"])

for i in text:
    if (len (i)>k):
        my_str.append(i)
print(my_str)


# Q90. Write a Python program to extract unique dictionary values.

# In[ ]:


sample_dict = {"vegetable": "potato", "fruit": "banana", "chocolate": "gems", "ABC": "gems"}

x=[]
for i in sample_dict.keys():
    x.append(sample_dict[i])
    
x=list(set(x))     # coverted list to set to remove all duplicate values and then again list to show in o/p.
print(x)


# Q91. Write a Python program to merge two dictionary.

# In[ ]:


sample_dict = {"vegetable": "potato", "fruit": "banana", "chocolate": "gems", "ABC": "gems"}
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

sample_dict.update(my_dict)
sample_dict


# Q92. Write a Python program to convert a list of tuples into dictionary.
# 
# Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}

# In[ ]:


tupl = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
my_dict = dict(tupl)
my_dict


# Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
# 
# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]

# In[ ]:


lst = [9, 5, 6]

result = [(i,i**3) for i in lst]      # we've made a list of tuple
result


# Q94. Write a Python program to get all combinations of 2 tuples.
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

# In[ ]:


test_tuple1 = (7, 2) 
test_tuple2 = (7, 8)

result1 =  [(i, j) for i in test_tuple1 for j in test_tuple2]  #1st "for" loop ll run once, then 2nd ll run completely
result2 =  [(x,y) for x in test_tuple2 for y in test_tuple1]
result = result1+result2
result


# Q95. Write a Python program to sort a list of tuples by second item.
# 
# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

# In[ ]:


lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
lst.sort(key = lambda x :x[1])
lst


# Q96. Write a python program to print below pattern.
# 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# In[ ]:


for i in range(1,6):
    print("* "*i)


# Q97. Write a python program to print below pattern.
# 
#     *
#    **
#   ***
#  ****
# *****

# In[ ]:


for i in range(1,6):
    print(" "*(5-i), "*"*i)


# Q98. Write a python program to print below pattern.
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# In[ ]:


for i in range(1,6):
    print(" "*(5-i), "* "*i)
    
OR
    
j=1
for i in range(5,0,-1):
    print(" "*i, end="")
    
    while j<6:
        print("* "*j)
        j=j+1
        break


# Q99. Write a python program to print below pattern.
# 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# In[ ]:


for i in range(1,6):
    a=1
    for j in range(i):
        print(f"{a} ", end ="")
        a=a+1
    print("\t")


# Q100. Write a python program to print below pattern.
# 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 

# In[74]:


a=1
for i in range(65,70):
    for j in range(a):
        print(f"{chr(i)} ", end ="")
    a=a+1
    print('\t')

