# Contoh Set
thisset = {"apple", "banana", "cherry"}
print(thisset)  # Output: {'apple', 'banana', 'cherry'} (urutan tidak terjamin)

# Set dengan nilai duplikat
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # Output: {'apple', 'banana', 'cherry'}

# True dan 1 dianggap sama
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)  # Output: {True, 'apple', 'banana', 'cherry', 2}

# False dan 0 dianggap sama
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)  # Output: {False, True, 'apple', 'banana', 'cherry'}

# Menghitung panjang set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))  # Output: 3

# Set dengan berbagai tipe data
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)  # Output: {'apple', 'banana', 'cherry'}
print(set2)  # Output: {1, 3, 5, 7, 9}
print(set3)  # Output: {False, True}

# Set dengan campuran tipe data
set1 = {"abc", 34, True, 40, "male"}
print(set1)  # Output: {'abc', 34, True, 40, 'male'}

# Mengecek tipe data set
myset = {"apple", "banana", "cherry"}
print(type(myset))  # Output: <class 'set'>


# Loop melalui set dengan for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)  # Output: apple, banana, cherry (urutan tidak terjamin)

# Mengecek apakah item ada dalam set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  # True

# Mengecek apakah item tidak ada dalam set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)  # False


# Menambahkan item ke set dengan add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Menambahkan item dari set lain dengan update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Menambahkan item dari iterable lain dengan update()
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# Menghapus item dengan remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # Output: {'apple', 'cherry'}

# Menghapus item dengan discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)  # Output: {'apple', 'cherry'}

# Menghapus item acak dengan pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)        # Output: item yang dihapus (acak, tidak pasti)
print(thisset)  # Output: sisa item dalam set (tidak berurutan)

# Mengosongkan set dengan clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # Output: set()

# Menghapus set sepenuhnya dengan del
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)  # Akan menghasilkan error karena set telah dihapus


# Loop melalui set dengan for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)  # Output: apple, banana, cherry (urutan tidak terjamin)


# Union beberapa set sekaligus
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)  # Output: gabungan semua item (urutan tidak terjamin)

# Union dengan operator |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)  # Output: {'a', 'b', 'c', 1, 2, 3}

# Metode update
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)  # output: {'a', 'b', 'c', 1, 2, 3}

# Intersection (hanya item duplikat)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)  # Output: {'apple'}

# dengan operator &
set3 = set1 & set2
print(set3)  # Output: {'apple'}

# Intersection update
set1.intersection_update(set2)
print(set1)  # Output: {'apple'}

# Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)  # Output: {'banana', 'cherry'}

# Difference dengan operator -
set3 = set1 - set2
print(set3)  # Output: {'banana', 'cherry'}

# Difference update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)  # Output: {'banana', 'cherry'}

# Symmetric Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {'banana', 'cherry', 'google', 'microsoft'}

# menggunakan operator ^
set3 = set1 ^ set2
print(set3)  # Output: {'banana', 'cherry', 'google', 'microsoft'}

# Symmetric Difference update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {'banana', 'cherry', 'google', 'microsoft'}

# Frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
# output: frozenset({'apple', 'banana', 'cherry'})
# <class 'frozenset'>
