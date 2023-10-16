# # def emp_details():
# #     employee_list={}
# #     python_list=[]
# #     devops_list=[]
# #     testing_list=[]
# #     java_list =[]
# #     dotnet_list = []
# #     num_of_employees=int(input("enter a number of employee:"))
# #     for i in range(num_of_employees):
# #         domain=input("enter a domain:")
# #         name=input("enter a empname:")
# #         empid=input("enter a empid:")
# #         email=input("enter a email:") 
# #         employee_details={"name":name,"empid":empid,"email":email}
# #         if domain=="python":
# #             python_list = python_list+[employee_details]
# #             employee_list["python"]=python_list
# #         elif domain =="devops":
# #             devops_list = devops_list+[employee_details]
# #             employee_list["devops"]=devops_list
# #         elif domain =="testing":
# #             testing_list = testing_list+[employee_details]
# #             employee_list["testing"]=testing_list
# #         elif domain == "java":
# #             java_list = java_list+[employee_details]
# #             employee_list["java"]=java_list
# #         elif domain == "dotnet":
# #             dotnet_list = dotnet_list+[employee_list]
# #             employee_list["dotnet"]=dotnet_list
# #     specific_domain=input("enter a domain:")
# #     print(employee_list [specific_domain])

# # emp_details()




# employee_data = {}
# def add_employee():
#     d = int(input("enter a number of employees :"))
#     for i in range (d):
#         domain = input("Enter the employee's domain: ")
#         name = input("Enter the employee's name: ")
#         empid = input("Enter the employee's empid: ")
#         email = input("Enter the employee's email: ")
#         employee_details = {"Name": name,"EmpID": empid,"Email": email}
#         employee_data[domain] = employee_details
#         print("Employee added successfully!")
# def print_employee_details():
#     domain = input("Enter the domain of the employee whose details you want to view: ")
#     employee_details = employee_data.get(domain)

#     if employee_details:
#         print("\nEmployee Details:")
#         for key, value in employee_details.items():
#             print(f"{key}: {value}")
#     else:
#         print("Employee not found.")
# add_employee ()
# print_employee_details ()

n = int(input("enter first number:"))
n1 = int(input("enter second number:"))
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True :
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        print("Invalid input. Please enter a number.")
        continue
    if choice == '1':
        print(n, "+", n1, "=", add(n, n1))

    elif choice == '2':
        print(n, "-", n1, "=", subtract(n, n1))

    elif choice == '3'
        print(n, "*", n1, "=", multiply(n, n1))
    
    elif choice == '4':
        print(n, "/", n1, "=", divide(n, n1))