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



# def function_name(gume):
#     print(gume)
# function_name("Dhana sekhar")


# def great(m):
#     print("hello",m,"welcome to my project")
# na = "dhana sekhar"
# great(na)


# def print(n):
#         l = []
#         for i in range(50):
#                 if i%2 == 0:
#                     l.append(i)
#         print(l)
# n = 50
# print(n)

# l = []
# for i in range (50):
#     if i%2 == 0:
#         l.append(i)
# print(l)



# def printingivennumber(n):
#     l = []
#     for i in range (50):
#         if i%2 == 0:
#             l.append(i)
#     print()
# n = 50
# printingivennumber(n)


# def display(*m):
#     for i in m:
#         print(i)
# display("Dhana","jamuna","yellamma")

# def sum (*n):
#     total = 0
#     for i in n:
#         total = total +i
#     print(total)
# sum(10,20,30,40,50,60)


# def display(**n):
#     for k,v in n.items():
#         print(k,":",v)
# display(name1 = "Dhana",name2 = "sekhar",name3 ="jamuna")
# display(name1 = "Dhana",name2 = "sekhar",name3 ="jamuna")


users = {'dhana':'1234','sekhar':'5678','amma':'0987','nana':'6543'}
def login():
    username = input("Enter your username")
    password = input("Enter your password")

    if username in users and users [username] == password :
        print ("login successfull")
    else :
        print (" Go to sinup page")