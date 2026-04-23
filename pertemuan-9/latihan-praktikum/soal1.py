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

    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def tampilkan_mundur(self):
        current = self.head

        while current and current.next:
            current = current.next

        while current:
            print(current.data)
            current = current.prev


dll = DoublyLinkedList()

dll.tambah_kendaraan("B 1234 ABC")
dll.tambah_kendaraan("D 5678 XYZ")
dll.tambah_kendaraan("A 9999 TUV")

print("[Maju]")
dll.tampilkan_maju()
print()
print("[Mundur]")
dll.tampilkan_mundur()