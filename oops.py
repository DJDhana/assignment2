# calculator program  

# class Calculator:
#     def add(self, a, b):
#         return a+b 
#     def subtract(self, a, b):
#         return a-b    
#     def multiply(self, a, b):
#         return a*b
#     def divide(self, a, b):
#         return a/b
# my_cl = Calculator()
# while True:
#     print("1: Add")
#     print("2: Subtract")
#     print("3: Multiply")
#     print("4: Divide")
#     print("5: Exit")

#     ch = int(input("Select operation: "))
#     if ch in (1, 2, 3, 4, 5):
#         if(ch == 5):
#             break       
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
        
# #         if(ch == 1):
# #             print(a, "+", b, "=", my_cl.add(a, b))
# #         elif(ch == 2):
# #             print(a, "-", b, "=", my_cl.subtract(a, b))
# #         elif(ch == 3):
# #             print(a, "*", b, "=", my_cl.multiply(a, b))
# #         elif(ch == 4):
# #             print(a, "/", b, "=", my_cl.divide(a, b))    
# #     else:
# #         print("Invalid Input")
# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#     def add_item(self, item_name, cost):
#         item = (item_name, cost)
#         self.items.append(item)
#     def remove_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#                 break
#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item[1]
#         return total
# cart = ShoppingCart()
# # cart.add_item("tv", 40000)
# # cart.add_item("ac",50000)
# # cart.add_item("shoes", 1500)
# # cart.add_item("shirt",2000)
# j = input("enter a items:")
# for item in j:
#     print(item[0], "=", item[1])
# total_cost = cart.calculate_total()
# print("Total cost:", total_cost)

# cart.remove_item("j")

# print("\nUpdated Items in Cart after removing j:")
# for item in cart.items:
#     print(item[0], "=", item[1])

# total_cost = cart.calculate_total()
# print("Total cost:", total_cost)
# shopping_list = []

# print("What should we buy from the shops")
# print("Enter 'DONE' to stop adding items")
# opping_list = []

# print("What should we buy from the shops")
# print("Enter 'DONE' to stop adding items")

# while True:
#     #asks for new items
#     new_item = input("ENTER A ITEMS:")

#     #be able to quit the app
#     if new_item == 'DONE':
#         break

#     #add items to shopping list
#     shopping_list.append(new_item)
# print("Here's your list:")
# for item in shopping_list:
#     print(item)
     


print("Welcome to the Shopping Cart Program!")
cart = []
while True:
    print()
    print ("Please type in one of these")
    print ("1. Add item ")
    print ("2. View cart ")
    print ("3. Remove Item ")
    print ("4  Total")
 
    select = int(input("select the number :"))
    item = ""
    if select == 1:
        while item != "ok":
            item = input(" What would you like to add:  ")
            price = float(input(" type in the price:"))
            sub=[item,price]
            cart.append(sub)
            print(f"'{item}' has been added to your cart.")
            print(f" The price is RS:{price}")
            break
    
    elif select == 2:
        print("This is your shopping cart")
        for item in cart:
            print(item)
        break         
    elif select == 3:
        takeout = input(" Type in what you would like to remove :")
        for i in cart:
            if i[0]==takeout:
                cart.remove(i)         
                 
    elif select == 4:
        sum=0
        for item in cart:
            sum=sum+item[1]
        print("Your total bill is ",sum)
        input ("type in ok when you're done: ")
        break
             
    if select == 5:
        print ("comeback soon.")
        
