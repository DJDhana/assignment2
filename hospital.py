class hospital:
    def __init__(self):
        self.data = []
        print ("welcome to hospital: ")

        self.options()
    def options (self):
        print(" 1 : Regetration :")
        print(" 2 : To view all of patient details")
        print(" 3 : Search data of patient")
        print(" 4 : To delete the data of patient")
        print(" 5 : To update the patient data ")
        print(" 6 : Exit")

        option = int(input("enter your option: "))
        if option == 1:
            self.regetration()
        elif option == 2:
            self.view()
        elif option == 3:
            self.search()
        elif option == 4:
            self.delete()
        elif option == 5:
            self.update()
        else :
            print("exit")

    def regetration(self):
        id = int(input("enter ID:"))
        if id in self.data:
            print("this id already taken")    
        else:
            name = input("Enter a name of the patient:")
            age = int(input("Enter a age of the patient:"))
            gender = input("Enter gender of the patient : ")
            issuse = input("Enter the issuse of the patient:")
            ref = [id,name,age,gender,issuse]
            self.data.append(ref)
            print("patient id has been updated")
            self.options()

    
    def view(self):
        if self.data == []:
            print("No patients are enrolled yet.")
        else:
            l=len(self.data)
            print("There are  patients in the hospital.")
            print(self.data)
            self.options()

    def search(self):
        id=int(input("Enter required id : "))
        if id in self.data:
            print(self.data[id])
        else:
            print("Given id is not in the list of the hospital")
        self.options()
    def delete(self):
        id=int(input("Enter required id: "))
        if id in self.data:
            self.data.remove[id]
            print("Patient data id",id ,"will be deleted succesfully.")
        else:
            print("Given id is not in the list of the hospital")
        self.options()
    def update(self):
        id=int(input("Enter required ID: "))
        if id in self.data:
            print ("choices:[1:name,2:age,3:gender,4:issuse]")
            choice = int(input("enter a choice: "))
            
            if choice == 1:
                new_name = input("New Name: ")
                self.data[id][1]=new_name
            elif choice==2:
                new_age = int(input("New Age: "))
                self.data[id][2]=new_age
            elif choice == 3:
                new_gender = input("New Gender: ")
                self.data[id][3]=new_gender
            elif choice == 4:
                new_issue = input("New Issue: ")
                self.data[id][4]=new_issue
            print("patient data will be updated succesfully..")
        else:
            print("the given id is not in the list of the hospital")
            self.options()

result = hospital() 