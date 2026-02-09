#Inheritance
# Ek class banao Vehicle jisme brand aur year ho. Phir ek child class Car banao jo Vehicle ko inherit kare aur usme fuel_type (e.g., Petrol/Electric) attribute add kare. Object bana kar saari details print karo.
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
class Vehicle2(Vehicle):
    def __init__(self, brand, year, fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type
    def all(self):
        return f"Brand: {self.brand} Year: {self.year} Fuel_type: {self.fuel_type}"
pro = Vehicle2("BMW", 2026, "Petrol")
print(pro.all())

#Method Over-riding
# Parent class Shape banao jisme ek method ho area() jo 0 return kare. Ab ek child class Square banao jo side input le aur area() method ko override karke side * side return kare.

class Shape:
    def area(self):
        return 0
class Square(Shape):
        def area(self, side):
             self.side = side
             return side * side
squared = Square()
print(squared.area(5))


# Ek Person class banao jisme name aur age ho. Ek Teacher class banao jo Person ko inherit kare. Teacher ke constructor mein super() ka use karke name aur age set karo aur ek naya attribute subject bhi add karo.

class Person:
     def __init__(self, name, age):
          self.name = name
          self.age = age
class Teacher(Person):
     def __init__(self, name, age, subject):
          super().__init__(name, age)
          self.subject = subject
detials = Teacher("Abdullah", 22, "Computer")
print(detials.name)
print(detials.age)
print(detials.subject)