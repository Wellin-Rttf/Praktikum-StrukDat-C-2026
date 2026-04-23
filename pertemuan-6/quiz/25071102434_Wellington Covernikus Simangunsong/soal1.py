def registrasi_gadget(merk, tipe, harga, sn):
    if harga > 1000000:
        if len(sn) >= 5:
            return {
                "merk" : merk,
                "tipe" : tipe,
                "harga" : harga,
                "sn" : sn,
                "status" : "Tersedia."
            }
        else:
            print("SN harus berisi minimal 5 karakter!")
            return None
    else:
        print("Harga gadget harus di atas 1.000.000!")
        return None

inventaris = []

for i in range(2):
    merk = input("Masukkan merk gadget: ")
    tipe = input("Masukkan tipe gadget: ")
    harga = float(input("Masukkan harga gadget: "))
    sn = input("Masukkan nomor SN gadget: ")
    print()
    gadget = registrasi_gadget(merk, tipe, harga, sn)
    inventaris.append(gadget)

    print(inventaris)