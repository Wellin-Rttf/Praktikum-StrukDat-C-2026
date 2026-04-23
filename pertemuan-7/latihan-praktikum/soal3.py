"""
 Case: Layanan Valet VIP tetap memungkinkan kendaraan untuk menyalip. 
Namun, karena keterbatasan sistem (Singly Linked List), petugas hanya bisa 
melihat kendaraan di depannya. Kendaraan VIP baru dapat disisipkan tepat di 
belakang kendaraan VIP tertentu yang sudah ada dalam antrean. Karena hanya 
satu arah, untuk pengecekan urutan, petugas harus membacanya dari kendaraan 
paling depan hingga paling belakang.
a. Tugas:
1. Gunakan struktur Singly Linked List (hanya memiliki pointer next).
2. Buat fungsi sisipkan_vip(plat_baru, plat_target): 
Mencari plat_target dalam antrean, lalu menyisipkan 
plat_baru tepat setelahnya.
3. Buat fungsi tampilkan_antrean() untuk menunjukkan urutan 
kendaraan dari depan ke belakang.
b. Logika: Menelusuri list dari head untuk mencari plat_target. Setelah 
ditemukan, buat node baru, hubungkan next dari node baru ke next milik 
target, lalu ubah next milik target ke node baru.
"""

class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None

def tampilkan_antrean(head):
    currentNode = head
    while currentNode:
        print(currentNode.plat, end=" -> ")
        currentNode = currentNode.next
    print("null")


def sisipkan_vip(head, plat_baru, plat_target):
    current = head

    while current:
        if current.plat == plat_target:
            nodeBaru = Node(plat_baru)
            nodeBaru.next = current.next
            current.next = nodeBaru
            return head
        current = current.next

    return head


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")

node1.next = node2
node2.next = node3


print("Antrean awal:")
tampilkan_antrean(node1)


node1 = sisipkan_vip(node1, "VIP 9999", "D 8888 XYZ")

print()
print("Setelah VIP disisipkan:")
tampilkan_antrean(node1)