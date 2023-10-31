# def calculator():
#     num1 = float(input("enter first number: "))
#     num2 = float(input("enter second number: "))
#     print ("press 1 for add")
#     print ("press 2 for sub")
#     print ("press 3 for mul")
#     print ("press 4 for div")

#     choice = int(input("enter your choice 1,2,3,4: "))

#     if choice == 1:
#         print(num1 + num2)
#     elif choice == 2:
#         print(num1 - num2)
#     elif choice == 3:
#         print(num1 * num2)
#     elif choice == 4:
#         print (num1 / num2)
#     else :
#         print ("invalid input")
# calculator ()


# employee = {}
# emp = int(input("enter a number of employee: "))
# for i in range (emp):
#     emp_id = input("Enter Employee ID: ")
#     name = input("Enter Employee Name: ")
#     designation = input("Enter Employee Designation: ")
#     email = input("Enter Employee Email: ")
    
#     employee [name] = {"name":name,"emp_id":emp_id,"designation":designation,"email":email}
#     print("Employee details added successfully!")
# def filter_details():
#     selected_name=input("enter a name:")
#     for key,value in employee.items():
#         if value["name"]==selected_name:
#             print(key,value)
# filter_details()