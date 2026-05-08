class HashTable:
    def __init__(self, size=10):
        # Menginisialisasi ukuran tabel
        self.size = size
        # Membuat tabel yang berisi list kosong (bucket) di setiap indeksnya
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        # Fungsi hash sederhana menggunakan fungsi bawaan hash() dan modulo
        # Modulo (%) memastikan indeks yang dihasilkan selalu berada dalam rentang ukuran tabel
        return hash(key) % self.size

    def insert(self, key, value):
        # 1. Hitung indeks menggunakan fungsi hash
        index = self._hash_function(key)
        bucket = self.table[index]

        # 2. Cek apakah key sudah ada di dalam bucket (untuk update nilai)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Jika key sama, update valuenya
                bucket[i] = (key, value)
                return

        # 3. Jika key belum ada, tambahkan (key, value) baru ke dalam bucket
        bucket.append((key, value))

    def get(self, key):
        # 1. Hitung indeks
        index = self._hash_function(key)
        bucket = self.table[index]

        # 2. Cari key di dalam bucket
        for k, v in bucket:
            if k == key:
                return v # Kembalikan value jika ditemukan

        return None # Kembalikan None jika key tidak ditemukan

    def delete(self, key):
        # 1. Hitung indeks
        index = self._hash_function(key)
        bucket = self.table[index]

        # 2. Cari key dan hapus jika ditemukan
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True # Berhasil dihapus

        return False # Gagal dihapus (key tidak ada)

    def display(self):
        print("--- Isi Hash Table ---")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")
        print("----------------------\n")

if __name__ == "__main__":
    # Membuat Hash Table dengan ukuran 5 agar collision lebih mudah terjadi dan terlihat
    ht = HashTable(size=5)

    # 1. Memasukkan Data
    print("1. Memasukkan data mahasiswa...")
    ht.insert("Budi", "NIM: 101")
    ht.insert("Siti", "NIM: 102")
    ht.insert("Agus", "NIM: 103")
    ht.insert("Rina", "NIM: 104")
    ht.insert("Joko", "NIM: 105")
    ht.display()

    # 2. Memasukkan data dengan key yang menghasilkan collision
    # (Tergantung fungsi hash Python, tapi dengan size=5 kemungkinan tabrakan tinggi)
    print("2. Update data (Siti)...")
    ht.insert("Siti", "NIM: 999 (Updated)")
    ht.display()

    # 3. Mengambil Data (Search)
    print("3. Mencari data:")
    print(f"Data Budi: {ht.get('Budi')}")
    print(f"Data Anton (Tidak ada): {ht.get('Anton')}\n")

    # 4. Menghapus Data
    print("4. Menghapus data (Agus)...")
    ht.delete("Agus")
    ht.display()
