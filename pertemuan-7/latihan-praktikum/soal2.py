"""
Case: Kendaraan yang sudah selesai urusan harus keluar melalui satu pintu yang 
sama. Karena ini antrean, kendaraan yang pertama datang harus pertama keluar
(FIFO). Namun, karena ada kendala teknis, terkadang ada kendaraan di urutan 
tertentu yang "mogok" dan harus dihapus dari daftar antrean secara paksa.
a. Tugas:
1. Buat struktur Node dan LinkedList.
2. Buat fungsi tambahKendaraan(plat) untuk menambah 
kendaraan ke akhir list (Tail).
3. Buat fungsi hapusKendaraan(plat) untuk menghapus kendaraan 
tertentu jika ia mogok di tengah antrean.
b. Logika: Melakukan traversal (penelusuran) dari head hingga menemukan 
plat yang cocok, lalu menyambungkan node sebelumnya langsung ke node 
sesudahnya.
"""

class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambahKendaraan(self, plat):
        newNode = Node(plat)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode

    def hapusKendaraan(self, plat):
        currentNode = self.head
        sebelumnya = None

        while currentNode:
            if currentNode.plat == plat:
                if sebelumnya is None:
                    self.head = currentNode.next
                else:
                    sebelumnya.next = currentNode.next
                return
            sebelumnya = currentNode
            currentNode = currentNode.next

    def tampilkan(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.plat, end=" -> ")
            currentNode = currentNode.next
        print("null")


parkir = LinkedList()

parkir.tambahKendaraan("B 1234 ABC")
parkir.tambahKendaraan("D 8888 XYZ")
parkir.tambahKendaraan("A 111 TUV")
parkir.tambahKendaraan("B 2022 EFG")

print("Antrean kendaraan:")
parkir.tampilkan()

parkir.hapusKendaraan("D 8888 XYZ")

print()
print("Setelah kendaraan mogok dihapus:")
parkir.tampilkan()
        


