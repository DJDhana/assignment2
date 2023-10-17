# #1.Write a Python script to add a key to a dictionary
# # simply dic {0:10,1:20}
# # expected dic {0:10,1:20,2:30}


# # dic = {0:10,1:20}
# # dic.update({2:30})
# # print(dic)


# #2.Write a Python script to check whether a given key already exists in a dictionary.

# # dict1 ={'dhana':70,'sekhar':80,'usha':50}
# # dict_check= 'jamuna'
# # if dict_check in dict1:
# #     print('The key already exists')
# # else:
# #     print('The key is not exists')

# #3.Write a Python program to iterate over dictionaries using for loops

# # my_dict = {'name':"Dhana", "company":"marolix", "city":"hyderabad"}
# # for key,value in my_dict.items():
# #     print(key,'=',value)




# #4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# #Sample Dictionary
# #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# # d = {}
# # for i in range(1,20):
# #     d[i] = i**2
# # print(d)

# #5.Write a Python program to create a dictionary from a string.
# #Note: Track the count of the letters from the string.
# #Sample string : 'marolix technology'
# #Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}

# # sample_string = "marolix technology"
# # my_dict ={}
# # for letters in sample_string:
# #     my_dict[letters]=my_dict.get(letters,0)+1
# # print(my_dict)





# #6. Write a Python program to sum all the items in a dictionary.

# # my_dict = {"a":200,"b":400,"c":600,"d":800}
# # total = 0
# # for i in my_dict.values():
# #     total = total + i
# # print(total)


# #7.Write a Python program to combine two dictionary by adding values for common keys.
# #d1 = {'a': 100, 'b': 200, 'c':300}
# #d2 = {'a': 300, 'b': 200, 'd':400}
# #Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# # d1 = {'a': 100, 'b': 200, 'c':300}
# # d2 = {'a': 300, 'b': 200, 'd':400}
# # d3 =dict(d1)
# # d3.update(d2)
# # for k ,v in d1.items():
# #     for x,y in d2.items():
# #         if k == x:
# #             d3[k]=(v+y)
# # print(d3)

# #8.Write a Python program to access dictionary key's element by index.
# #Expected Output:
# #physics
# #math
# #chemistry

# # my_dict = {"physics":50,"math":60,"chemistry":70}
# # print(list(my_dict)[0])
# # print(list(my_dict)[1])
# # print(list(my_dict)[2])

# #9.Write a Python program to remove a key from a dictionary.

# # my_dict ={'dhana':203,'likitha':260,'radhika':821}
# # my_dict.pop("likitha")
# # print(my_dict)                        


# #10.Write a Python script to merge two Python dictionaries.
# # dict1 ={'DHANA':50,'usha':40}
# # dict2 ={'daddy':100,'mother':30}
# # dict3 =dict2.copy()
# # dict3.update(dict1)
# # print(dict3)


shopping_list = []

def show_help():
    print('What should we pick up at the store?')
    print("""
  Enter 'DONE' to stop adding items.
  Enter 'REMOVE' to remove from the list
  Enter 'SHOW' to see your shopping list
  """)
def add_to_list(item):
    shopping_list.append(item)
    print('{} was added to your shopping list!'.format(item))
    print('You have {} items on your list.'.format(len(shopping_list)))

def remove_list():
    shopping_list.remove(item)
    print (shopping_list)
# Create a function to print all the items in the shopping list
def show_list():
    print('My Shopping List:')
    for item in shopping_list:
        print(item)

while True:
    new_item = input('> ')

    if new_item == 'DONE':
        break
    elif new_item == 'REMOVE':
        remove_list()
        break
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)
show_list()