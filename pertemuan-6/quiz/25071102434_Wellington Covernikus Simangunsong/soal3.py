

def update_stok(katalog, sn_target, jumlah_tambah):
    katalog = [
    {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2}, 
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} ]
    x = input("Masukkan SN: ")
    if x in update_stok["sn"]:
        update_stok["sn" + 1]

    daftar_merk = {}
    for i in update_stok["merk"]:
        daftar_merk.add(i)

for i in range(2):
    update_stok()