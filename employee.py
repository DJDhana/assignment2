# # employee_details = {}
# # def add_employee():
# #     domain = input("Enter the employee's domain: ")
# #     name = input("Enter the employee's name: ")
# #     employee_id = input("Enter the employee's ID: ")
# #     email = input("Enter the employee's email: ")
# #     employee_details[employee_id] = {'Domain': domain, 'Name': name, 'Email': email}
# # def print_employee_details(employee_id):
# #     if employee_id in employee_details:
# #         details = employee_details[employee_id]
# #         print("Employee ID:", employee_id)
# #         print("Domain:", details['Domain'])
# #         print("Name:", details['Name'])
# #         print("Email:", details['Email'])
# #     else :
# #          print("Employee not found!")        
# # while True:
# #     print("\nOptions:")
# #     print("1. Add Employee")
# #     print("2. Print domain ")    
# #     choice = input("Enter your choice (1/2): ")    
# #     if choice == '1':
# #         add_employee()
# #     elif choice == '2':
# #         employee_id = input("Enter Employee ID: ")
# #         print_employee_details(employee_id)
# #         break
# #     else:
# #         print("Invalid choice. Please choose 1 or 2")

# # print("Program terminated.")



# employee_data = {}

# # Function to add an employee
# def add_employee():
#     domain = input("Enter the employee's domain: ")
#     name = input("Enter the employee's name: ")
#     empid = input("Enter the employee's empid: ")
#     email = input("Enter the employee's email: ")

#     # Create a dictionary to store the employee's details
#     employee_details = {
#         "Domain": domain,
#         "Name": name,
#         "EmpID": empid,
#         "Email": email
#     }

#     # Add the employee's details to the main dictionary
#     employee_data[empid] = employee_details
#     print("Employee added successfully!")

# # Function to print employee details
# def print_employee_details():
#     empid = input("Enter the empid of the employee whose details you want to view: ")
#     employee_details = employee_data.get(empid)

#     if employee_details:
#         print("\nEmployee Details:")
#         for key, value in employee_details.items():
#             print(f"{key}: {value}")
#     else:
#         print("Employee not found.")
