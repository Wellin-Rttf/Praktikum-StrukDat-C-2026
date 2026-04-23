"""
 Case: Sebuah sistem parkir mencatat plat nomor kendaraan yang masuk dalam 
sebuah array. Kamu diminta untuk memisahkan kendaraan berdasarkan aturan 
ganjil-genap.
a. Input: ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
b. Tugas:
1. Buat fungsi yang menerima array tersebut.
2. Identifikasi angka terakhir pada plat nomor (abaikan huruf di belakang).
3. Pisahkan menjadi dua array baru: ganjil dan genap.
c. Logika: Mengambil karakter angka terakhir dari string dan menggunakan 
operator modulus (%).
"""

plat_nomor = []
while True:
    input_plat = input("Masukkan plat nomor kendaraan (0 jika ingin berhenti): ")
    if input_plat == "0":
        break
    plat_nomor.append(input_plat)

ganjil = []
genap = []

for i in plat_nomor:
    a = i.split(" ")
    b = a[1]  
    c = int(b[-1]) 

    if c % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)


print(f"Plat nomor: {plat_nomor}")
print(f"Plat ganjil: {ganjil}")
print(f"Plat genap: {genap}")