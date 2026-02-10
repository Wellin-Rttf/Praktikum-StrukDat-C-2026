
# Contoh tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry')

# Tuple dengan duplikat
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')

# Panjang tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # Output: 3

# Tuple dengan satu item
thistuple = ("apple",)
print(type(thistuple))  # Output: <class 'tuple'>

# Akan dideteksi sebagai string
thistuple = ("apple")
print(type(thistuple))  # Output: <class 'str'>

# Tuple dengan berbagai tipe data
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Tuple campuran tipe data
tuple4 = ("abc", 34, True, 40, "male")

# Mengecek tipe data tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  # Output: <class 'tuple'>


# Mengakses item tuple dengan indeks
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # Output: banana
# Catatan: indeks pertama adalah 0

# Negative indexing (mengakses dari belakang)
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  # Output: cherry

# Range of indexes (mengambil sebagian item)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Output: ('cherry', 'orange', 'kiwi')

# Range tanpa start (otomatis dari awal)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])  # Output: ('apple', 'banana', 'cherry', 'orange')

# Range tanpa end (otomatis sampai akhir)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])  # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Range dengan negative indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # Output: ('orange', 'kiwi', 'melon')

# Mengecek apakah item ada di dalam tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")  
    # Output: Yes, 'apple' is in the fruits tuple


# Mengubah nilai tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  # Output: ('apple', 'kiwi', 'cherry')

# Menambahkan item ke tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'orange')

# Menambahkan item ke tuple (gabung tuple dengan tuple)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'orange')

# Menghapus item dari tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)  # Output: ('banana', 'cherry')

# Menghapus tuple sepenuhnya
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # akan menampilkan error karena tuple sudah dihapus


# Meng-unpack tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Menggunakan Asterisk* (menyimpan sisa nilai ke dalam list)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)   # Output: apple
print(yellow)  # Output: banana
print(red)     # Output: ['cherry', 'strawberry', 'raspberry']

# Menggunakan Asterisk* (asterisk bukan di akhir)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)   # Output: apple
print(tropic)  # Output: ['mango', 'papaya', 'pineapple']
print(red)     # Output: cherry


# Loop melalui tuple dengan for loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)  # Output: apple, banana, cherry (dicetak baris per baris)

# Loop melalui index numbers dengan range() dan len()
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])  # Output: apple, banana, cherry (dicetak baris per baris)

# Loop dengan while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])  # Output: apple, banana, cherry (dicetak baris per baris)
    i = i + 1


# Menggabungkan dua tuple dengan operator +
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)

# Mengalikan isi tuple dengan operator *
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
