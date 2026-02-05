barang = ("B001", "Laptop Gaming", 15000000)

print(barang[2])

barang[3] = 14000000        
# #Tuple tidak dapat diubah value-nya, jadi item yang terdapat pada tuple tidak dapat ditambah, diubah, atau dikurangi sehingga akan menampilkan error

#Tetapi kita dapat mengubah tuple menjadi llist, lalu list tersebut dimodifikasi dan diubah lagi menjadi tuple


listBarang = list(barang)
listBarang[2] = 14000000
barang = tuple(listBarang)

print(barang)
