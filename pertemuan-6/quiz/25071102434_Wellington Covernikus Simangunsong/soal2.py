stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
]

def filter_harga(data, min_harga, max_harga):
    list = []
    for i in stok_gadget:
        if stok_gadget["harga"] >= min_harga:
            if stok_gadget["harga"] >= max_harga:
                list.append(i)
                return list
        else:
            return list

def main():
    int(input("Masukkan batas bawah: "), filter_harga.min_harga)
    int(input("Masukkan batas atas: "), filter_harga.max_harga)

    if list == []:
        print("Tidak ada gadget dalam rentang harga tersebut.")
    else:
        print(filter_harga())

main()