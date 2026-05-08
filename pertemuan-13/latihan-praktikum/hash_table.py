class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, kode, judul):
        index = self._hash_function(kode)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == kode:
                bucket[i] = (kode, judul)
                print(f"Buku '{kode}' diperbarui menjadi '{judul}'")
                return

        bucket.append((kode, judul))
        print(f"Buku '{kode}: {judul}' berhasil ditambahkan")

    def search(self, kode):
        index = self._hash_function(kode)
        bucket = self.table[index]

        for k, v in bucket:
            if k == kode:
                print(f"Ditemukan {k} : {v}")
                return v

        print(f"Buku dengan kode {kode} tidak ditemukan")
        return None

    def delete(self, kode):
        index = self._hash_function(kode)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == kode:
                del bucket[i]
                print(f"Buku '{kode} : {v}' berhasil dihapus")
                return True

        print(f"Buku dengan kode '{kode}' tidak ditemukan")
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")
            else:
                print(f"Index {i}: []")
        print("\n")
        

ht = HashTable()

print("Insert data buku")
ht.insert("BK111", "Mahir C++ Dalam Satu Jam")
ht.insert("BK222", "Python Dasar")
ht.insert("BK333", "Matematika Diskrit")
ht.insert("BK444", "Atomic Habits")
ht.insert("BK555", "1984")
ht.insert("BK668", "Aksi Massa")
print()

print("Display isi hash table")
ht.display()

print("Insert data baru")
ht.insert("BK045", "Mein Kampf")
ht.insert("BK111", "Bumi Manusia")

print("\nDisplay setelah update")
ht.display()

print("Search buku")
ht.search("BK333")
ht.search("BK111")
ht.search("BK999")

print("\nDelete buku")
ht.delete("BK222")

print("\nDisplay buku")
ht.display()
