class Student:
    #class variable
    uni = "oxford"


    def get_name(self,s_name,s_age, s_city):
        self.name = s_name
        self.age = s_age
        self.city = s_city
        print(self.name)
        print(self.age)
        Print(self.city)

john = Student()
john.get_name("John",10)

print(john.uni)


#mike = Student()
#mike.get_name("Mike",10)
#an object variable belongs to an object
