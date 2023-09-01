#1.Write a Python function that accepts a string and counts the number of upper and lower case letters Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

# def counting_upper_lower_case(string):
#     upper_char = 0
#     lower_char = 0
#     for char in string :
#         if char . isupper():
#             upper_char = upper_char+1
#         elif char . islower():
#             lower_char = lower_char+1
#     print(upper_char)
#     print(lower_char)
# counting_upper_lower_case("The quick Brow Fox")

#2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

# def sorting_list(n):
#     new_list = []
#     for num in n:
#         if num not in new_list:
#             new_list .append(num)
#     print(new_list)
# n = [1,2,3,3,3,3,4,5]
# sorting_list(n)   


#3.Write a Python function to check whether a string is a pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog".

# def pangram(str):
#   str = str.lower()
#   for letter in "abcdefghijklmnopqrstuvwxyz":
#     if letter not in str:
#       return False
#   return True
# str = input("enter input string:")
# if pangram(str):
#   print("the string is in pangram")
# else:
#   print (" the string is not a pangram ")

#4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).

# def listvalues():
#     l = list()
#     for i in range(0,11):
#         l.append(i**2)
#     print(l)
# listvalues()


#5.Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20 

# def sum(*n):
#     total = 0
#     for i in n:
#         total = total + i
#     print(total)
# sum (8,2,3,0,7)


# def sum(n):
#     add = 0
#     for num in n:
#         add = add + num
#     print((add))
# sum([8,2,3,0,7])


#6.write a function to find sum of given values, pass values has variable number of arguments to function.

# def sum_of_values(*args):
#     total = 0
#     for num in args:
#         total += num
#     print(total)
# sum_of_values(10,20,30,40,45)  

