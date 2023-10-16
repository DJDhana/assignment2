# Write a recursive function that accepts a number as its argument and returns the sum of digits.

# def sumdigits(n):
#     if (n<10):
#         return 1
#     else :
#         return n%10 + sumdigits(n//10)
# numbers = 9596979899
# print(sumdigits(numbers))


# Write a recursive function that calculate sum of first n natural numbers

# def sum(n):
#     if (n == 0):
#         return 1
#     else:
#         return n + sum(n - 1)
# number = 100
# print(sum(number))


# fibonacci series

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else :
#         return fib(n-1) + fib (n-2)
# for i in range (10):
#     print(fib(i),end = " ")

# Lambda function 

# Lambda function finding min number
# min = lambda a, b : a if(a < b) else b
# print(min(10, 20))

# Lambda example with adding two arguments
# add = lambda x, y : x + y
# print(add(10, 20))  

# # Lambda example with sub two arguments

# sub = lambda x , y : x - y
# print(sub(90,20))


### filter function

# finding the even number and odd numbers

# seq = [0, 1, 2, 3, 5, 8, 13,78,33,96,34,20,28]
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

# defining function to test if entered age is above 20 or not

# def eligible(age):
#   if age >= 20 :
#      return True
# ages = [12, 22, 18, 32, 9, 5, 82, 96, 14,7]
# returnedIterable = filter(eligible, ages)
# print(list(returnedIterable))

# creating a function that will return True if the number is divisible by 6
# def divisible(i):
#     if i%6==0:
#         return True
#     else:
#         return False
# nums = [23,18,396,12,96,126,172,963]
# divisible_by_6 = filter(divisible, nums)
# print(list(divisible_by_6))