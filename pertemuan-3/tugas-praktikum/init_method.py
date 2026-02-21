# Contoh penggunaan __init__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)          # Output: Emil
print(p1.age)           # Output: 36


# Contoh class tanpa init
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)          # Output: Tobias
print(p1.age)           # Output: 25


# Contoh dengan dengan init
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)          # Output: Linus
print(p1.age)           # Output: 28


# Nilai default dalam init
class Person:
  def __init__(self, name, age=18):     # Nilai dalam parameter age di-assign dengan 18
    self.name = name
    self.age = age

p1 = Person("Emil")                     # Sehingga saat tidak dispesifikkan pada object p1 ini, maka akan digunakan nilai default
p2 = Person("Tobias", 25)

print(p1.name, p1.age)      # Output: Emil 18
print(p2.name, p2.age)      # Output: Tobias 25


# Multiple parameter dalam init
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)              # Output: Linus
print(p1.age)               # Output: 30
print(p1.city)              # Output: Oslo
print(p1.country)           # Output: Norway
