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