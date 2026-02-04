# Logic Building(Learning)
class Laptop:
    def __init__(self, brand, processor, ram, price):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.price = price
    def display_specs(self):
        print(f"This laptop is {self.brand} with core {self.processor} and with a storage of {self.ram}")
    def check_budget(self, budget):
        if budget >= self.price:
            print("You can buy this Laptop.")
        else:
            print("its expensive.")

my_laptop = Laptop("Hp", "i5", "8GB", 100000)
print(my_laptop.brand)
print(my_laptop.processor)
print(my_laptop.ram)
print(my_laptop.price)
my_laptop.display_specs()
my_laptop.check_budget(50000)


# Challenge 1: The "Smart Bulb" (Logic Building)
class SmartBulb:
    def __init__(self,):
        self.is_on = False

    def turn_on(self):
        print("Bulb is shinning..")
    def turn_off(self):
        print("Darkness Everywhere..")

bulb = SmartBulb()
bulb.turn_on()


# Challenge 2: The "Bank App" (Data Handling)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insaf kro!")
        else:
            self.balance -= amount
            print(self.balance)

check = BankAccount(1000)
check.withdraw(1100)

# Challange 3:
class Student:
    def __init__(self, name, marks_list):
        self.name = name
        self.marks_list = marks_list

    def calculate_average(self):
        avg = sum(self.marks_list) / len(self.marks_list)
        return avg
    def final_report(self):
        average = self.calculate_average()
        if average > 50:
            print("Pass")
        else:
            print("Fail")
sty = Student("Abdullah", [70,80,90])
print(sty.calculate_average())
sty.final_report()


# Challenge 4:
class Store:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity =quantity
        self.revenue = 0
    def material(self, stock):
        self.quantity += stock
        return self.quantity
    def purchase(self, amount):
        if amount < self.quantity:
            self.quantity -= amount
            self.revenue = self.price * amount
        else:
            print("Out of Stock...")
    def Total_records(self):
        print(f"Product name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Revenue: {self.revenue}")

prn = Store("Abdullah", 1000, 10)
print(prn.material(21))
prn.purchase(15)
prn.Total_records()