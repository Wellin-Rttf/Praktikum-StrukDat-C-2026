# Contoh penggunaan parameter self
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()              # Output: Hello, my name is Emil


# Alasan menggunakan self
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()          # Output: Tobias
p2.printname()          # Output: Linus

# self dapat diganti menggunakan kata lain
class Person:
  def __init__(myobject, name, age):       # self diganti myobject
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()              # Output: Hello, my name is Emil


# Mengakses atribut dengan self
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()          # Output: 2020 Toyota Corolla


# Memanggil method dengan self
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()      # Memanggil method greet menggunakan self
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()        # Output: Hello, Tobias! Welcome to our website.
