# class princepal:
#     def princepal_work (self):
#         print ("princepal given work to HOD")
# class HOD (princepal):
#     def hod_work (self):
#         print ("HOD given work to the students")
# class students (HOD):
#     def students_work (self):
#         print("studetds are doing work:")
# a = students()
# a.princepal_work()
# a.hod_work()
# a.students_work()

# class Father:
#     def Driving (self):
#         print ("my father is a driver")
# class Mother :
#     def Housewife (self):
#         print("my mother is a housewife")
# class child (Father,Mother):
#     def playing (self):
#         print("they are enjoing their life")

# b = child()
# b.Driving()
# b.Housewife()
# b.playing()


# class Father:
#     def father(self):
#         print ("this is the father of this two guys")
# class Child_1 (Father):
#     def Dhana(self):
#         print("I am the son of the my father")
# class Child_2 (Father):
#     def Liki(self):
#         print ("I am the daugther of the my father")


# d1 = Child_1()
# d1.Dhana()
# d1.father()

# d2 = Child_2()
# d2.Liki()
# d2.father() 


class Hospital:
    def _init_(self):
        self.data = []
        print("Welcome to our hospital. Please select an option")
        self.options()

    def options(self):
        print("Select 1 to enroll\nSelect 2 for overall patients view\nSelect 3 to search patient data\nSelect 4 to delete patient data\nSelect 5 to update patient data")
        option = int(input("Enter your option: "))
        if option == 1:
            self.enroll()
        elif option == 2:
            self.overall_patients_view()
        elif option == 3:
            self.search()
        elif option == 4:
            self.delete()
        elif option == 5:
            self.update()
        else:
            print("Thank you...")

    def enroll(self):
        id = int(input("Enter ID: "))
        if any(patient[0] == id for patient in self.data):
            print("This ID number has already been taken.")
        else:
            name = input("Enter patient name: ")
            age = input("Enter age: ")
            temp = input("Enter temperature: ")
            illness = input("Enter the health issue: ")
            res = [id, name, age, temp, illness]
            self.data.append(res)
            print("Patient with ID", id, "has been enrolled successfully.")
        self.options()

    def overall_patients_view(self):
        if not self.data:
            print("No patients are enrolled yet.")
        else:
            print(f"There are {len(self.data)} patients in the hospital.")
            for patient in self.data:
                print(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Temp: {patient[3]}, Illness: {patient[4]}")

        self.options()

    def search(self):
        id = int(input("Enter required ID: "))
        found = False
        for patient in self.data:
            if patient[0] == id:
                print(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Temp: {patient[3]}, Illness: {patient[4]}")
                found = True
                break

        if not found:
            print("Given ID is not yet enrolled in the hospital")
        self.options()

    def delete(self):
        id = int(input("Enter required ID: "))
        found = False
        for patient in self.data:
            if patient[0] == id:
                self.data.remove(patient)
                print(f"Patient data with ID {id} has been deleted successfully.")
                found = True
                break

        if not found:
            print("Given ID is not yet enrolled in the hospital")
        self.options()

    def update(self):
        id = int(input("Enter required ID: "))
        found = False
        for patient in self.data:
            if patient[0] == id:
                print("Choices: [1: Name, 2: Age, 3: Temp, 4: Illness]")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    patient[1] = input("Enter new name: ")
                elif choice == 2:
                    patient[2] = input("Enter new age: ")
                elif choice == 3:
                    patient[3] = input("Enter new temperature: ")
                elif choice == 4:
                    patient[4] = input("Enter new illness: ")
                else:
                    print("Invalid choice.")
                print(f"Patient data with ID {id} has been updated successfully.")
                found = True
                break

        if not found:
            print("Given ID is not yet enrolled in the hospital")
        self.options()

result = Hospital()
