"""
Diberikan list stok barang di gudang: stok_barang = [15, 40, 30, 10, 25]
a. Temukan indeks dari nilai 10, lalu ubah nilai pada indeks tersebut menjadi 50.
b. Tambahkan nilai 5 ke akhir list, kemudian urutkan list secara descending (besar ke 
kecil).
c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
d. Gunakan shorthand if (ternary) untuk menampilkan "Stok Aman" jika rata-rata nilai 
dalam list > 20, jika tidak tampilkan "Waspada"
"""


stok_barang = [15, 40, 30, 10, 25]

print(stok_barang.index(10))

stok_barang[3] = 50
print(stok_barang)

stok_barang.append(5)
stok_barang.sort(reverse=True)
print(stok_barang)

print(sum(stok_barang))

print("Stok Aman") if (sum(stok_barang) / len(stok_barang)) > 20 else print("Waspada")