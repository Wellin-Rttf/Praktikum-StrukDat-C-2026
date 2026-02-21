# Membuat class sederhana
class MyClass:
  x = 5

# Membuat object
p1 = MyClass()
print(p1.x)            # Output: 5

# Menghapus object menggunakan keyword del
del p1

print(p1)              # Output: error (NameError: 'p1' is not defined)

# Multiple object
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)             # Output: 5
print(p2.x)             # Output: 5
print(p3.x)             # Output: 5

# Statement/pernyataan pass untuk menhindari error saat membuat class kosong
class Person:
  pass