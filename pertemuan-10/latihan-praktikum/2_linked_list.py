# Bagian 2: Implementasi Menggunakan Linked List
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def isEmpty(self):
        return self.top == None

    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.isEmpty():
            return "Riwayat kosong"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url

    def peek(self):
        if self.isEmpty():
            return "Riwayat kosong"
        return self.top.url

    def Size(self):
        return self.count

myStack = StackLinkedList()

print("==== Riwayat Navigasi Browser ====")
while True:
    url = input("Halaman baru dikunjungi (ketik 0 untuk berhenti): ")
    myStack.push(url)
    if url == "0":
        break
    
    print("Halaman terakhir: ", myStack.peek())

while True:
    back = input("Ketik 'Back' untuk kembali ke halaman web sebelumnya: ").lower()
    if back == "back":
        myStack.pop()
        print("Halaman web: ", myStack.peek())
    else:
        break