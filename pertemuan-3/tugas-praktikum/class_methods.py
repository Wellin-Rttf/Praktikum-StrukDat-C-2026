# Contoh class dengan method greet()
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):          # Method harus memiliki parameter self
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()          # Output: Hello, my name is Emil


# Method dengan parameter
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))       # Output: 8
print(calc.multiply(4, 7))  # Output: 28


# Metode mengakses properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())        # Output: Tobias is 28 years old


# Method mengubah property
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()     # Output: Happy birthday! You are now 26
p1.celebrate_birthday()     # Output: Happy birthday! You are now 27


# Method khusus str
# Contoh method tanpa str:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)                   # Output: <__main__.Person object at ...>

# Method dengan str:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)               # Output: Tobias (36)


# Multiple method dalam sebuah class
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Progressive House")
my_playlist.add_song("Levels")
my_playlist.add_song("UMF Anthem")
my_playlist.show_songs()


# Menghapus method
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet()  # Akan menghasilkan error karena metode greet sudah dihapus





