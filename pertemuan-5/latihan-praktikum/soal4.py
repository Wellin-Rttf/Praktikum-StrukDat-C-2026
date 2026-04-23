"""
Diberikan data produk dalam bentuk list of dictionaries:
gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]
a. Tambahkan satu key baru bernama "kategori" dengan nilai "Aksesoris" untuk produk 
Keyboard.
b. Tambahkan satu item baru: "Headset" dengan harga 350000 dan stok 8.
c. Hitung Total Nilai Aset (Harga x Stok) untuk setiap item. Tampilkan output dengan 
format:
Item: [Nama] | Total Aset: Rp [Hasil Perkalian]
"""

gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20} ]

gudang_pc[1]["kategori"] = "Aksesories"
print(gudang_pc[1])

gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})
print(gudang_pc[3])

for x in gudang_pc:
    total = x["harga"] * x["stok"]
    print(f"Item: {x["harga"]} | Total Aset: Rp{total}")