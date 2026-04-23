"""
Diberikan list berisi tuple data mahasiswa dan poin keaktifan: data_aktivitas = [("Diki", 
88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
a. Lakukan perulangan pada list tersebut. Jika poin > 80, tampilkan: "[Nama] 
mendapatkan predikat Gold". Jika poin 50-80, tampilkan: "[Nama] mendapatkan 
predikat Silver". Di bawah itu, tampilkan: "[Nama] mendapatkan predikat Bronze"
"""


data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

tuple1, tuple2, tuple3, tuple4 = data_aktivitas

for x in data_aktivitas:
    nama, poin = x

    if poin > 80:
        print(f"{nama} mendapatkan predikat Gold")
    elif 50 >= poin <= 80:
        print(f"{nama} mendapatkan predikat Silver")
    else:
        print(f"{nama} mendapatkan predikat Bronze")