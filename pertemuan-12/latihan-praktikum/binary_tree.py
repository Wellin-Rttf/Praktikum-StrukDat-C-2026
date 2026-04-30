class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("A")

        self.root.left = Node("B")
        self.root.right = Node("C")

        self.root.left.left = Node("D")
        self.root.left.right = Node("E")

        self.root.right.right = Node("F")
    
    def get_leaf_nodes(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.data, end=" ")
            self.get_leaf_nodes(node.left)
            self.get_leaf_nodes(node.right)

def traverse_preorder(node):
    if node is None:
        return
    print(node.data, end=" - ")
    traverse_preorder(node.left)
    traverse_preorder(node.right)
    
def traverse_inorder(node):
    if node is None:
        return
    traverse_inorder(node.left)
    print(node.data, end=" - ")
    traverse_inorder(node.right)

def traverse_postorder(node):
    if node is None:
        return
    traverse_postorder(node.left)
    traverse_postorder(node.right)
    print(node.data, end=" - ")


tree = BinaryTree()

print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
print("======================================")

tree.insert_manual()

print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.")

print("HASIL AUDIT:")
print("1. Pre-Order :", end=" ")
traverse_preorder(tree.root)
print()
print("2. In-Order :", end=" ")
traverse_inorder(tree.root)
print()
print("3. Post-Order :", end=" ")
traverse_postorder(tree.root)
print()

print("\n[DATA] Gudang Ujung (Leaf Nodes):", end=" ")
tree.get_leaf_nodes(tree.root)
print()

print("======================================")
print("Audit Selesai!")