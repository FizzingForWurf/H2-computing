class Pet():
    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, type):
        self.__animal_type = type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

class Car():
    def __init__(self, model, make):
        self.__year_model = model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5

    def get_speed(self):
        return self.__speed

class PersonalInfo():
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address
        
    def get_age(self):
        return self.__age
        
    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name
        
    def set_address(self, address):
        self.__address = address
        
    def set_age(self, age):
        self.__age = age
        
    def set_phone(self, phone):
        self.__phone = phone

class RetailItem():
    def __init__(self, description, inventory, price):
        self.__description = description
        self.__inventory = inventory
        self.__price = price

    def get_description(self):
        return self.__description
        
    def get_inventory(self):
        return self.__inventory
        
    def get_price(self):
        return self.__price

def questionOne():
    name = input("Enter the name of your pet: ")
    type = input("Enter the animal type: ")
    age = int(input("Enter your pet's age: "))

    myPet = Pet(name, type, age)

    print(myPet.get_name())
    print("Animal Type:", myPet.get_animal_type())
    print("Age:", myPet.get_age())

def questionTwo():
    car = Car(2001, "Nissan")
    
    for i in range(5):
        car.accelerate()
        print(car.get_speed())

    print()

    for i in range(5):
        car.brake()
        print(car.get_speed())

def questionThree():
    me = PersonalInfo("Zheng Hong", "Somewhere", 17, 12345678)
    dad = PersonalInfo("Dad", "Somewhere", 50, 12345678)
    friend = PersonalInfo("djsfa", "fjkas", 18, 67843465)

def questionFour():
    jacket = RetailItem("Jacket", 12, 59.95)
    jeans = RetailItem("Designer Jeans", 40, 34.95)
    shirt = RetailItem("Shirt", 20, 24.95)
    items = [jacket, jeans, shirt]

    print("%-10s%-20s%-16s%-6s" % ("", "Description", "Inventory", "Price"))
    for i in range(3):
        print("%-10s%-20s%-16d%-0.2f" % ("Item " + str(i+1), items[i].get_description(), items[i].get_inventory(), items[i].get_price()))

def main():
    #questionOne()
    #questionTwo()
    #questionThree()
    questionFour()

main()