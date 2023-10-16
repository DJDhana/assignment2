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
        
#         if(ch == 1):
#             print(a, "+", b, "=", my_cl.add(a, b))
#         elif(ch == 2):
#             print(a, "-", b, "=", my_cl.subtract(a, b))
#         elif(ch == 3):
#             print(a, "*", b, "=", my_cl.multiply(a, b))
#         elif(ch == 4):
#             print(a, "/", b, "=", my_cl.divide(a, b))    
#     else:
#         print("Invalid Input")

class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item_name, cost):
        item = (item_name, cost)
        self.items.append(item)
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
cart = ShoppingCart()
cart.add_item("tv", 40000)
cart.add_item("ac",50000)
cart.add_item("shoes", 1500)
cart.add_item("shirt",2000)
print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "=", item[1])
total_cost = cart.calculate_total()
print("Total cost:", total_cost)

cart.remove_item("ac")

print("\nUpdated Items in Cart after removing ac:")
for item in cart.items:
    print(item[0], "=", item[1])

total_cost = cart.calculate_total()
print("Total cost:", total_cost)
