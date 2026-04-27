class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            return None

        temp = self.head
        self.head = self.head.next
        self._size -= 1

        if self.head is None:
            self.tail = None

        return temp

    def peek(self):
        if self.isEmpty():
            return None
        return self.head

    def isEmpty(self):
        return self._size == 0

    def size(self):
        return self._size

    def printQueue(self):
        temp = self.head
        nomor = 1

        while temp:
            print(f"{nomor}. {temp.nama} -> {temp.keluhan}")
            temp = temp.next
            nomor += 1

    def clear(self):
        while not self.isEmpty():
            self.dequeue()


myQueue = Queue()

print("""====================================
SISTEM ANTRIAN POLI UMUM
RS Sehat Bersama
====================================""")

if myQueue.isEmpty():
    antrian = "YA, antrian masih kosong"
else:
    antrian = "Tidak, antrian tidak kosong"

print(f"[CEK] Apakah antrian kosong? {antrian}")

myQueue.enqueue("Budi", "demam tinggi")
print(f"[DAFTAR] Budi terdaftar dengan keluhan: demam tinggi (No. Antrian: {myQueue.size()})")

myQueue.enqueue("Ani", "batuk pilek")
print(f"[DAFTAR] Ani terdaftar dengan keluhan: batuk pilek (No. Antrian: {myQueue.size()})")

myQueue.enqueue("Citra", "sakit kepala")
print(f"[DAFTAR] Citra terdaftar dengan keluhan: sakit kepala (No. Antrian: {myQueue.size()})")

print(f"[INFO] Jumlah myQueue menunggu: {myQueue.size()} orang")

p = myQueue.peek()
print(f"[PEEK] myQueue berikutnya: {p.nama} (keluhan: {p.keluhan})")

dipanggil = myQueue.dequeue()
print(f"[PANGGIL] Dokter memanggil: {dipanggil.nama} (keluhan: {dipanggil.keluhan})")

myQueue.enqueue("Dodi", "nyeri perut")
print(f"[DAFTAR] Dodi terdaftar dengan keluhan: nyeri perut (No. Antrian: {myQueue.size()})")

print("[ANTRIAN SAAT INI]")
myQueue.printQueue()

dipanggil = myQueue.dequeue()
print(f"[PANGGIL] Dokter memanggil: {dipanggil.nama} (keluhan: {dipanggil.keluhan})")

print(f"[INFO] Jumlah myQueue masih menunggu: {myQueue.size()} orang")

myQueue.clear()
print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

if myQueue.isEmpty():
    antrian = "YA, antrian masih kosong"
else:
    antrian = "Tidak, antrian tidak kosong"

print(f"[CEK] Apakah antrian kosong? {antrian}")