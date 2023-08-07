# print positive number or negitive 
#a = int (input(" enter a number:"))
#if a>=0:
    #print("the given number is positive")
#else:


   # print("the given number is negitive")
# take two number which one is greater 
#a = int (input("enter a number:"))
#b = int (input("enter a number:"))
#if a > b:
    #print("a is greater than b ")
#elif b > a:
    #print("b is grather than a")


# take a string repat it 5 times

#for i in range(5):
    #print("DHANA SEKHAR")


# take a string repat it 5 times

#i=0
#while i<=5: 
    #print("DHANASEKHAR")
    #i+=1

# take a string print a half string  

#a = "Dhanasekhar"
#b = len(a)//2
#print(a[:b])

# take a string print a half string  

#a = "Dhanasekhar"
#b = a[len(a)//2:]
#print(b)

# check the student pass or fail

#a = int (input("enter a marks:"))
#if a <=34:
    #print("fail")
#elif a >=35:
    #print("pass")

# check the eligible for vote or not

#a = int(input("enter a age:"))
#if a >=18:
  #  print("eligible")
#else:
    #print("not eligible")

# check the length and breath is equal to square or not

#a = input("enter a length:")
#b = input("enter a breath:")
#if  a == b:
    #print ("square")
#else:
    #print("not square")

# print even numbers

# for i in range (0,101):
    #if i % 2==0:
        #print(i)

# print odd numbers

#for i in range(0,101):
    #if i % 2 !=0:
        #print(i)

#pattern programs

#num = int(input("enter a value:"))
#for i in range(1,num+1):
    #for j in range(1,i+1):
        #print("*",end=" ")
    #print( )
    
#pattern programs

#num = int(input("enter a value:"))
#for i in range(0,num):
    #for j in range (0,num-i-1):
        #print(end=" ")
    #for k in range (0,i+1):
        #print("*",end="")
    #print(  )


####1.Write a python program to remove character from string    


#D = "Dhana sekhar is a very gud boy "
#D1 =D.replace("very","")
#print(D1)

# 2.Write a program to check String is Palindrome or not

#string = input("enter a string:")
#revstr = ""
#for i in string:
    #revstr = i + revstr
#if (string == revstr):
    #print("the given string is palindrome")
#else:
    #print ("the given string is not a palindrome")


#3.Write a python program to check given character is vowel or consonant

#D = input("enter a char:")
#if (D == 'a' or D == 'e' or D == 'i' or D == 'o' or D == 'u' or D == 'A' or D == 'E' or D == 'I' or D == 'O' or D == 'U'):
 #   print(D,"is a vowles")
#else:
#    print(D,"is a consonant")


# 4.Write a python program to replace string space with given character in Python

#s="am working in marolix"
#s2=s.replace(" ","the")
#print(s2)

#5.Write a python program to count alphabets, digits, and special characters in the string

#string = input("Enter a String : ")
#alphabets=0
#digits=0
#specialChars=0
#for i in string: 
    		#if i.isalpha():
       			 #alphabets+=1
    		#elif i.isdigit():
        			#digits+=1
    		#else:
        			#specialChars+=1
#print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)

#6.Write a python program to remove all the blank spaces in a given string
#string = "coders hub  "
#new_string = string.replace(" ", "")
#print(new_string)

#7.Write a python program to find sum of integers in the string
str1 = input('Enter a string: ')
sum=0
for i in str1:
    if i.isdigit(): 
        sum=sum+int(i)
print("sum=",sum)


#8.Write a python program to Remove Repeated Character from String.
#string="marolix technology solution"
#p=""
#for char in string:
	#if char not in p:
		#p=p+char
#print(p)

#9.Write a python program to count occurrence of given character in string.

#count = 0
#my_string = "dhanasekhar"
#my_char = "a"
#for i in my_string:
    #if i == my_char:
        #count += 1
#print(count)

#10.Write a python program to check string is anagrams or not in Python.
#str1 = "race"
#str2 = "care"
#if(len(str1) == len(str2)):
    #sorted_str1 = sorted(str1)
    #sorted_str2 = sorted(str2)
    #if(sorted_str1 == sorted_str2):
        #print(str1 + " and " + str2 + " are anagram.")
    #else:
        #print(str1 + " and " + str2 + " are not anagram.")
#else:
    #print(str1 + " and " + str2 + " are not anagram.")

#11.Write a Program to Sort the Characters of the String and First Alphabet Symbols followed by Numeric Values.
#string=input("Enter a string: ")
#alpha=[] 
#digit=[] 
#for c in string:
    #if c.isalpha():
        #alpha.append(c)  
    #else:
        #digit.append(c)
#result=''.join(sorted(alpha)+sorted(digit)) 
#print(result)