

# Membuat dictionary sederhana
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Mengakses item dictionary dengan key
print(thisdict["brand"])  # output: Ford

# Dictionary dengan key duplikat
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)  
# output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Menghitung jumlah item dalam dictionary
print(len(thisdict))  # output: 3

# Dictionary dengan berbagai tipe data sebagai value
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)


# Mengakses item dictionary dengan key secara langsung
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])  # output: Mustang

# Mengakses item dictionary dengan metode get()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)  # output: Mustang

# Mendapatkan semua key dalam dictionary
x = thisdict.keys()
print(x)  # output: dict_keys(['brand', 'model', 'year'])

# Perubahan pada dictionary akan tercermin pada daftar keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)  # sebelum perubahan

car["color"] = "white"
print(x)  # setelah perubahan, dict_keys(['brand', 'model', 'year', 'color'])


# Mendapatkan semua value dalam dictionary
x = thisdict.values()
print(x)  # output: dict_values(['Ford', 'Mustang', 1964])

# Perubahan pada dictionary akan tercermin pada daftar values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) # sebelum perubahan

car["year"] = 2020
print(x) # setelah perubahan


# Mengubah nilai item dictionary dengan key secara langsung
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)  
# output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Mengubah nilai item dictionary dengan metode update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)  
# output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# Menambahkan item baru ke dictionary dengan key baru
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)  
# output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# Menghapus item dictionary dengan pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# output: {'brand': 'Ford', 'year': 1964}

# Menghapus item terakhir dengan popitem()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# output: {'brand': 'Ford', 'model': 'Mustang'}

# Menghapus item dengan keyword del
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# output: {'brand': 'Ford', 'year': 1964}

# Menghapus dictionary sepenuhnya dengan del
del thisdict
print(thisdict)  # error, karena dictionary sudah dihapus

# Mengosongkan dictionary dengan clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# output: {}


# Looping dictionary - menampilkan semua key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
# output: brand, model, year

# menampilkan semua value dengan akses key
for x in thisdict:
  print(thisdict[x])
# output: Ford, Mustang, 1964

# menampilkan semua value dengan values()
for x in thisdict.values():
  print(x)
# output: Ford, Mustang, 1964

# menampilkan semua key dengan keys()
for x in thisdict.keys():
  print(x)
# output: brand, model, year

# menampilkan key dan value dengan items()
for x, y in thisdict.items():
  print(x, y)
# output:
# brand Ford
# model Mustang
# year 1964


# Membuat salinan dictionary dengan metode copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Membuat salinan dictionary dengan fungsi dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



# Contoh nested dictionary
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)

# Membuat nested dictionary dari beberapa dictionary terpisah
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)

# Mengakses item dalam nested dictionary
print(myfamily["child2"]["name"])  # output: Tobias

# Looping nested dictionary
for x, obj in myfamily.items():
  print(x)  # key utama (child1, child2, child3)
  for y in obj:
    print(y + ':', obj[y])  # key dan value di dalam nested dictionary
