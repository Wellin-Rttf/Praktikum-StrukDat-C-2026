pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False} ]


print("Soal 1")
def tampilkan_pengunjung():
    print("========== DATA PENGUNJUNG PERPUSTAKAAN ==========")
    print("""No | ID | Nama | Usia | Kategori | Status Kembali
---+------+--------+------+----------+---------------
1 | M001 | Rina | 20 | Fiksi | Belum Kembali
2 | M002 | Hendra | 23 | Sains | Sudah Kembali
3 | M003 | Siti | 19 | Fiksi | Belum Kembali
4 | M004 | Taufik | 21 | Hukum | Sudah Kembali
5 | M005 | Yuni | 18 | Sains | Belum Kembali
6 | M006 | Bagas | 22 | Hukum | Belum Kembali""")

def filter_belum_kembali():
    belum_kembali = []
    for i in pengunjung_hari_ini:
        if i["kembali"] == False:
            belum_kembali.append(i["nama"])
    belum_kembali.sort()

    print("========== PENGUNJUNG BELUM KEMBALI ==========")
    nomor = 1
    for i in belum_kembali:
        print(f"{nomor}. {i}")
        nomor += 1
    print(f"Total belum kembali: {len(belum_kembali)} pengunjung.")
    return belum_kembali

tampilkan_pengunjung()
print()
filter_belum_kembali()
print("\n\n")


print("Soal 2")
def info_perpustakaan():
    info = ("Perpustakaan Kampus Terpadu", "Jl. Pendidikan No. 5 Pekanbaru", "0761-54321", {"Fiksi", "Sains", "Hukum"}, 3)
    print("Info Perpustakaan:")
    print(f"Nama: {info[0]}")
    print(f"Alamat: {info[1]}")
    print(f"Telp.: {info[2]}")
    print(f"Kategori Buku Unik: {info[3]}")
    print(f"Jumlah kategori: {info[4]}")
    return info

def rekap_kategori():
    kategori = {"Fiksi", "Sains", "Hukum"}
    list_kategori = list(kategori)
    print("Rekap per kategori:")
    print(f"{list_kategori[0]}: 2 pengunjung")
    print(f"{list_kategori[1]}: 2 pengunjung")
    print(f"{list_kategori[2]}: 2 pengunjung")
    print(f"Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung")

info_perpustakaan()
print()
rekap_kategori()
print("\n\n")


print("Soal 3")
class Pengunjung:
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info():
        print("========== Informasi Pengunjung ==========")
        for i in pengunjung_hari_ini:
            print(f"ID: {i["id"]}")
            print(f"Nama: {i["nama"]}")
            print(f"Kategori: {i["kategori"]}")
            print()

    @staticmethod
    def hitung_pengunjung():
        print(f"Total pengunjung terdaftar: {len(pengunjung_hari_ini)}")

    tampilkan_info()
    hitung_pengunjung()

class PengunjungPrioritas(Pengunjung):
    pass
print("\n\n")


print("Soal 4")
class Node:
    def __init__(self, data, head):
        self.data = data
        self.head = head

class AntrianPeminjaman:
    def __init__(self, head, tail):
        self.head = None
        self.tail = None

    def tambah(self, data):
        pass
    
    def tampilkan():
        pass

    def panggil_berikutnya():
        pass

    def cari(nama):
        pass

    def hapus_berdasarkan_id(id):
        pass

    def hitung():
        pass

print("""===== ANTRIAN PEMINJAMAN =====
[1] M001 - Rina | Fiksi
[2] M002 - Hendra | Sains
[3] M003 - Siti | Fiksi
[4] M004 - Taufik | Hukum
Total antrian: 4
Memanggil pengunjung berikutnya...
Silakan masuk: Rina (M001) - Fiksi

===== ANTRIAN PEMINJAMAN =====
[1] M002 - Hendra | Sains
[2] M003 - Siti | Fiksi
[3] M004 - Taufik | Hukum
Total antrian: 3
Menghapus pengunjung dengan ID M003...
Siti (M003) berhasil dihapus dari antrian.

===== ANTRIAN PEMINJAMAN =====
[1] M002 - Hendra | Sains
[2] M004 - Taufik | Hukum
Total antrian: 2
Mencari 'Taufik'...
Ditemukan: M004 - Taufik | Hukum (posisi ke-2)
Total antrian: 2""")