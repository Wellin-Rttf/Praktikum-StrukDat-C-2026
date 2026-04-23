class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        baru = Node(data)

        if not self.head:
            # Node pertama menunjuk ke dirinya sendiri
            self.head = baru
            baru.next = baru
        else:
            # Cari node terakhir (tail)
            tail = self.head
            while tail.next != self.head:
                tail = tail.next

            # Sisip di akhir
            tail.next = baru
            baru.next = self.head

    def delete(self, target):
        if not self.head:
            print("List kosong.")
            return

        curr = self.head
        prev = None

        while True:
            if curr.data == target:
                # Jika hanya satu node
                if curr.next == self.head and prev is None:
                    self.head = None
                    return

                # Jika hapus head
                if curr == self.head:
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next

                    self.head = curr.next
                    tail.next = self.head
                else:
                    prev.next = curr.next

                return

            prev = curr
            curr = curr.next

            # Sudah keliling satu putaran
            if curr == self.head:
                break

        print(f"Data {target} tidak ditemukan.")

    def display(self):
        if not self.head:
            print("List kosong.")
            return

        p = self.head
        while True:
            print(p.data, end=" -> ")
            p = p.next
            if p == self.head:
                break
        print("(kembali ke head)")


# Membuat objek
cll = CircularLinkedList()

# Insert data
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

# Tampilkan isi list
print("Isi list:")
cll.display()

# Hapus data
cll.delete(20)

# Tampilkan lagi
print("Setelah hapus 20:")
cll.display()

# Hapus head
cll.delete(10)

print("Setelah hapus head (10):")
cll.display()

# Hapus data yang tidak ada
cll.delete(99)