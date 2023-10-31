## write a program to merge two list

# x = ["usha","gurrappa","likitha"]
# y = ["dhana","sekhar"]
# x.extend(y)
# print(x)

#how to find sum of list

#num = [10,20,30,40,50]
#print(sum(num))

#print  even numbers from list

# d = [10,20,30,40,5,24,71,21,34,56,87,96,113]
# list =[]
# for i in d:
#     if i % 2 == 0:
#         list.append(i)
# print(list)
        

# print odd numbers given list

# d = [10,20,30,40,5,24,71,21,34,56,87,96,113]
# list =[]
# for i in d: 
#     if i % 2 != 0:
#         list.append(i)
# print(list)
        

## delete element of given index

# j = ["dhana","sekhar","usha","likitha","gurrappa"]
# j.remove("sekhar")
# print(j)

## delete element directly from a given list

# j = ["dhana","sekhar","usha","likitha","gurrappa"]
# j.pop(1)
# print(j)

# inser a element at a given index 

# l = ["Dhana","sekhar","likitha","gurrappa"]
# l.insert(3,"usha")
# print(l)

# inser a element at a given index at a end

# l = ["Dhana","sekhar","likitha","gurrappa"]
# l.append("usha")
# print(l)


## check the size of two list are same or not 

# lst1=int(input("enter the size1:" ))
# lst2=int(input("enter the size2:"))
# new_list1=[]
# new_list2=[]
# for i in range(0,lst1):
#    element1=int(input("enter the element:"+str(i)+":"))
#    new_list1.append(element1)
# print(new_list1)
# for j in range(0,lst2):
#   element2=int(input("enter the element:"+str()+":"))
#   new_list2.append(element2)
# print(new_list2)
# if len(new_list1)==len(new_list2):
#     print("length are equal")
# else:
#     print("length are not equal")

#1.Write a Python script to add a key to a dictionary
# simply dic {0:10,1:20}
# expected dic {0:10,1:20,2:30}


# dic = {0:10,1:20}
# dic.update({2:30})
# print(dic)


#2.Write a Python script to check whether a given key already exists in a dictionary.

# dict1 ={'dhana':70,'sekhar':80,'usha':50}
# dict_check= 'jamuna'
# if dict_check in dict1:
#     print('The key already exists')
# else:
#     print('The key is not exists')

#3.Write a Python program to iterate over dictionaries using for loops

# my_dict = {'name':"Dhana", "company":"marolix", "city":"hyderabad"}
# for key,value in my_dict.items():
#     print(key,'=',value)




#4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# d = {}
# for i in range(1,20):
#     d[i] = i**2
# print(d)

#5.Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'marolix technology'
#Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}

# sample_string = "marolix technology"
# my_dict ={}
# for letters in sample_string:
#     my_dict[letters]=my_dict.get(letters,0)+1
# print(my_dict)





#6. Write a Python program to sum all the items in a dictionary.

# my_dict = {"a":200,"b":400,"c":600,"d":800}
# total = 0
# for i in my_dict.values():
#     total = total + i
# print(total)


#7.Write a Python program to combine two dictionary by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 =dict(d1)
# d3.update(d2)
# for k ,v in d1.items():
#     for x,y in d2.items():
#         if k == x:
#             d3[k]=(v+y)
# print(d3)

#8.Write a Python program to access dictionary key's element by index.
#Expected Output:
#physics
#math
#chemistry

# my_dict = {"physics":50,"math":60,"chemistry":70}
# print(list(my_dict)[0])
# print(list(my_dict)[1])
# print(list(my_dict)[2])

#9.Write a Python program to remove a key from a dictionary.

# my_dict ={'dhana':203,'likitha':260,'radhika':821}
# my_dict.pop("likitha")
# print(my_dict)                        


#10.Write a Python script to merge two Python dictionaries.
# dict1 ={'DHANA':50,'usha':40}
# dict2 ={'daddy':100,'mother':30}
# dict3 =dict2.copy()
# dict3.update(dict1)
# print(dict3)
