# Contoh sebuah properties dalam sebuah class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)          # Output: Emil
print(p1.age)           # Output: 36


# Mengakses properti
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)       # Output: Toyota
print(car1.model)       # Output: Corolla


# Mengubah nilai pada properti
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)       # Output: 25

p1.age = 26
print(p1.age)       # Output: 26


# Menghapus sebuah properti
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name)  # Output: Linus
#print(p1.age)   # Akan menghasillkan error karena properti age sudah dihapus


# Class properties and object properties
class Person:
  species = "Human"  # Class property

  def __init__(self, name):
    self.name = name  # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)          # Output: Emil
print(p2.name)          # Output: Tobias
print(p1.species)       # Output: Human
print(p2.species)       # Output: Human


# Mengubah Class Properties
class Person:
  lastname = ""         # Class property

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Bergling"

print(p1.lastname)      # Output: Bergling
print(p2.lastname)      # Output: Bergling


# Menambahkan properti baru
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25             # Properti age ditambahkan
p1.city = "Oslo"        # Properti city ditambahkan

print(p1.name)          # Output: Tobias
print(p1.age)           # Output: 25
print(p1.city)          # Output: Oslo
