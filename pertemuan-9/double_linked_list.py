class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        baru = Node(data)
        if not self.head:
            # List kosong
            self.head = baru
            self.tail = baru
        else:
            # Sisip di akhir
            baru.prev = self.tail
            self.tail.next = baru
            self.tail = baru

    def delete(self, target):
        hapus = self.head
        while hapus:
            if hapus.data == target:
                # Jika bukan head
                if hapus.prev:
                    hapus.prev.next = hapus.next
                else:
                    # hapus adalah head
                    self.head = hapus.next

                # Jika bukan tail
                if hapus.next:
                    hapus.next.prev = hapus.prev
                else:
                    # hapus adalah tail
                    self.tail = hapus.prev

                del hapus
                return

            hapus = hapus.next

        print(f"Data {target} tidak ditemukan.")

    def display_forward(self):
        if not self.head:
            print("List kosong.")
            return

        p = self.head
        while p:
            print(p.data, end=" <-> ")
            p = p.next
        print("None")

    def display_backward(self):
        if not self.tail:
            print("List kosong.")
            return

        p = self.tail
        while p:
            print(p.data, end=" <-> ")
            p = p.prev
        print("None")


# Membuat objek
dll = DoubleLinkedList()

# Insert data
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

# Tampilkan dari depan
print("Forward:")
dll.display_forward()

# Tampilkan dari belakang
print("Backward:")
dll.display_backward()

# Hapus data
dll.delete(20)

print("Setelah hapus 20:")
dll.display_forward()
dll.display_backward()

# Hapus head
dll.delete(10)

print("Setelah hapus head (10):")
dll.display_forward()

# Hapus tail
dll.delete(40)

print("Setelah hapus tail (40):")
dll.display_forward()

# Hapus data yang tidak ada
dll.delete(99)