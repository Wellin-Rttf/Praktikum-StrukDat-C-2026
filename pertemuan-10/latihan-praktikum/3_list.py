# Bagian 3:  Iplementasi Menggunakan List
list_url = []

print("==== Riwayat Navigasi Browser ====")

# isEmpty
isEmpty = not bool(list_url)
print("Url kosong: ", isEmpty)

# Push
while True:
    url = input("Halaman baru dikunjungi (ketik 0 untuk berhenti): ")
    list_url.append(url)
    if url == "0":
        list_url.pop()
        break
print("\nList riwayat web: ", list_url)

# Peek
topElement = list_url[-1]
print("Halaman terakhir: ", topElement)
print()

# Pop
while True:
    back = input("Ketik 'Back' untuk kembali ke halaman web sebelumnya: ").lower()
    if back == "back":
        if len(list_url) == 0: 
            print("Riwayat kosong")
        else:
            poppedElement = list_url.pop()
            print("Halaman di-pop: ", poppedElement)
            topElement = list_url[-1] if list_url else "Tidak ada"
            print("Halaman web: ", topElement)
    else:
        break

# Stack after Pop
print("\nUrl setelah di-pop: ", list_url)

# Size
print("Ukuran: ", len(list_url))
print(list_url)