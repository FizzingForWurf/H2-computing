class Employee():
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number
    
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, rate):
        super().__init__(name, number)
        self.__shift = shift
        self.__rate = rate

    def get_shift(self):
        return self.__shift

    def get_rate(self):
        return self.__rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_rate(self, rate):
        self.__rate = rate

class ShiftSupervisor(Employee):
    def __init__(self, name, number, salary, bonus):
        super().__init__(name, number)
        self.__salary = salary
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary
        
    def get_bonus(self):
        return self.__bonus

class Person():
    def __init__(self, name, address, num):
        self.__name = name
        self.__address = address
        self.__num = num

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address
        
    def get_number(self):
        return self.__num

class Customer(Person):
    def __init__(self, name, address, number, mail):
        super().__init__(name, address, number)
        self.__mail = mail

    def get_mail(self):
        return self.__mail

    def set_mail(self, mail):
        self.__mail = mail

def questionOne():
    name = input("Enter worker's name: ")
    number = int(input("Enter worker's phone number: "))
    shift = input("Enter shift: ")
    pay = float(input("Enter hourly pay rate: "))

    worker = ProductionWorker(name, number, shift, pay)

    print(worker.get_name())
    print("Contact number:", worker.get_number())
    if worker.get_shift() == 1:
        print("Day Shift")
    else:
        print("Night Shift")
    print("Hourly pay rate:", worker.get_rate())

def questionTwo():
    supervisor = ShiftSupervisor("Tom", 12345678, 100000, 100)

    print(supervisor.get_name())
    print(supervisor.get_number())
    print(supervisor.get_salary())
    print(supervisor.get_bonus())

def questionThree():
    man = Customer("Tom", "Singapore", 12345678, True)

    print(man.get_name())
    print(man.get_address())
    print(man.get_number())
    if man.get_mail():
        print(man.get_name(), "is on the mailing list!")
    else:
        print(man.get_name(), "is NOT on the mailing list!")

def main():
    questionOne()
    questionTwo()
    questionThree()

main()