class BST:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

def insert(node, id_buku, judul):
    if node is None:
        return Node(id_buku, judul)
    else:
        if id_buku < node.id_buku:
            node.left = insert(node.left, id_buku, judul)
        elif id_buku > node.id_buku:
            node.right = insert(node.right, id_buku, judul)
    return node

def traversal_inorder(node, counter=0):
    if node is None:
        return counter
    counter = traversal_inorder(node.left, counter)
    counter += 1
    print(f"{counter}. {node.id_buku} - {node.judul}")
    counter = traversal_inorder(node.right, counter)
    return counter

def search(node, target):
    if node is None:
        return None
    elif node.id_buku == target:
        return node
    elif target < node.id_buku:
        return search(node.left, target)
    else:
        return search(node.right, target)

def get_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def get_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

def height(node):
    if node is None:
        return -1
    left_h = height(node.left)
    right_h = height(node.right)
    return max(left_h, right_h) + 1



print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=========================================")

tree = BST()
tree.root = insert(tree.root, 50, "Dasar Pemrograman")
print("[INSERT] Berhasil memasukkan: ID 50 - Dasar Pemrograman")
tree.root = insert(tree.root, 30, "Struktur Data")
print("[INSERT] Berhasil memasukkan: ID 30 - Struktur Data")
tree.root = insert(tree.root, 70, "Kecerdasan Buatan")
print("[INSERT] Berhasil memasukkan: ID 70 - Kecerdasan Buatan")
tree.root = insert(tree.root, 20, "Matematika Diskrit")
print("[INSERT] Berhasil memasukkan: ID 20 - Matematika Diskrit")
tree.root = insert(tree.root, 40, "Basis Data")
print("[INSERT] Berhasil memasukkan: ID 40 - Basis Data")
tree.root = insert(tree.root, 60, "Jaringan Komputer")
print("[INSERT] Berhasil memasukkan: ID 60 - Jaringan Komputer")
tree.root = insert(tree.root, 80, "Sistem Operasi")
print("[INSERT] Berhasil memasukkan: ID 80 - Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal):")
traversal_inorder(tree.root)

print()
for i in (60, 100):
    print(f"[SEARCH] Mencari ID {i}...")
    node = search(tree.root, i)
    if node:
        print(f"Ditemukan! Judul: {node.judul}")
    else:
        print("Data tidak ditemukan.")

print(f"\n[STATISTIK] ID Terkecil: {get_min(tree.root).id_buku}")
print(f"[STATISTIK] ID Terbesar: {get_max(tree.root).id_buku}")

print(f"\n[INFO] Tinggi (Height) Tree: {height(tree.root)}")
print("=========================================")
print("Simulasi Selesai!")
