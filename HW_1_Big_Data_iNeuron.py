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

# print("iNeuron"*4)

# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

# a = int(input("Enter a number"))
# if(a%2==0):
#     print("even")
# else:
#     print("odd")

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

# b = int(input("Enter your age"))
# if(b >= 18):
#     print("I can vote")
# else:
#     print("I can't vote")

# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```

# def my_function(number):
#     sum = 0
#     for i in number:        
#         if(i%2 == 0):
#             sum = sum + i            
#     return(sum)
#     
# numbers = [12, 75, 150, 180, 145, 525, 50]
# c = my_function(numbers)
# print(c)

# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

# x,y,z = input("Enter 3 no's").split()
# print(max(x,y,z))

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

# def my_function(number):
#     for i in number:
#         if(i%5==0):
#             if(i>150):
#                 continue
#             elif(i>500):
#                 break
#             print(i)
#                 
# 
# numbers = [12, 75, 150, 180, 145, 525, 50]
# my_function(numbers)
