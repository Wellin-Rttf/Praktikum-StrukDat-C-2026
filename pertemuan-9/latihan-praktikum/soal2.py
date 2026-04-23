class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def hapus_kendaraan(self, plat):
        current = self.head

        while current:
            if current.data == plat:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next

                    if current.next:
                        current.next.prev = current.prev
                return
            current = current.next

    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


dll = DoublyLinkedList()

dll.tambah_kendaraan("B 1111 AA")
dll.tambah_kendaraan("D 2222 BB")
dll.tambah_kendaraan("A 3333 CC")
dll.tambah_kendaraan("B 4444 DD") 

print("Sebelum:") 
dll.tampilkan_maju()

dll.hapus_kendaraan("A 3333 CC") 
print()

print("Sesudah:") 
dll.tampilkan_maju()

