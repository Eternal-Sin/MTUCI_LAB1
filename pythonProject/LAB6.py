import hashlib #библиотека для хэширования

#1
class UserAccount:

    def __init__(self,username,email,password):
        self._username = username
        self._email = email
        self.__password = password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self,exam_password):
        return  self.__password == UserAccount.hash_password(exam_password)

    def set_password(self, current_password):
        if self.check_password(current_password):
            new_password = input("New password: ")
            self.__password = UserAccount.hash_password(new_password)
            print("Password changed")
        else:
            print("error")
            account1.set_password(input("Enter password:"))


account1 = UserAccount("user1","1@mail.ru", UserAccount.hash_password("111"))

account1.set_password(input("Enter password:"))

if(input("Restart? Y/N: ").upper() == "Y"):
    account1.set_password(input("Enter password:"))
else:
    print("Stop")

#2

class Vehicle:

    def __init__(self,make,model):
        self.make = make
        self.model = model

    def get_info(self):

        return self.make,self.model
class Car(Vehicle):

    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)

        self.fuel_type = fuel_type

    def get_info(self):
        return self.make, self.model,self.fuel_type

