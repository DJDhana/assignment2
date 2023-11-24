# s="Dhanasekhar"
# print(s.count("a"))

# m = "Dhana@ sekhar"
# n = m.replace("@","")
# print(n)

# str1 = "Race"
# str2 = "Care"
# str1 = str1.lower()
# str2 = str2.lower()
# if (len(str1)) == (len(str2)):
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)

#     if(sorted_str1 == sorted_str2):
#         print(str1 + "and" +str2+ "are anagram")
#     else:
#         print(str1 +"and" +str2+ "are not anagram")
# else:
#     print(str1 +"and" + str2 +" are not anagram")


# string = input("Enter a string:")
# if (string == string[::-1]):
#     print ("The given string is palindrom")
# else:
#      print ("The given string is not palindrom")

# string = input("Enter a string:")
# revstr = ""
# for i in string:
#     revstr = i+revstr
# print("Revered string :",revstr)

# if (string == revstr):
#     print("the given string is palindrom")
# else:
#      print ("The given string is not palindrom")

# ch = input("Enter a character:")
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# if ch in vowels:
#     print("the given character is a vowel")
# else:
#     print("the given character is not a vowel")

# string = "Dhana sekhar"
# ch = "-"
# string = string.replace(" ",ch)
# print(string)

# string = input("Enter a string:")
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# res =""
# for i in range(len(string)):
#     if string [i] not in vowels:
#         res = res+string[i]
# print(res)


# str = input("Enter a string:")
# vowels=0
# consonates=0
# for i in str:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='O' or i=='I' or i=='U'):
#         vowels=vowels+1
#     else:
#         consonates=consonates+1
# print("The number of vowles:",vowels)
# print("The number of consonates:",consonates)

# str = input("Enter a string:")
# ch = input("Enter a symbol:")
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# new_str=''
# for i in str:
#     if i in vowels:
#         new_str += ch
#     else:
#         new_str += i
# print(new_str)


# str = "Dhanasekhar"
# p =""
# for i in str:
#     if i not in p:
#         p =p+i
# print(p)



str = "dhanasekhar"
l = len(str)
f = 0
for i in range(l):
    f = 0
    for j in range (l):
        if str[i] == str[j] and i!=j:
            f=1
            break
    if f ==0:
        print ("first non-repeating character is :",str[i])
        break
    if f ==1:
        print("no non-repeating character") 

