import heapq

class Graph:
    def __init__(self):
        self.adj = {}

    def tambah_kota(self, nama):
        if nama not in self.adj:
            self.adj[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)
        self.adj[u].append((v, jarak))
        self.adj[v].append((u, jarak))
        print(f"[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)")

    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")
        for kota, tetangga in self.adj.items():
            koneksi = ", ".join(f"{t} ({j})" for t, j in tetangga)
            print(f"{kota} terhubung ke: {koneksi}")

    def graph_dijkstra(self, kota_asal):
        print(f"\n[PROSES] Menghitung rute terpendek dari: {kota_asal}...")

        INF = float('inf')
        jarak = {kota: INF for kota in self.adj}
        jarak[kota_asal] = 0

        pq = [(0, kota_asal)]
        dikunjungi = set()

        while pq:
            jarak_kini, CN = heapq.heappop(pq)

            if CN in dikunjungi:
                continue
            dikunjungi.add(CN)

            for tetangga, bobot in self.adj[CN]:
                if tetangga not in dikunjungi:
                    jarak_baru = jarak[CN] + bobot
                    if jarak_baru < jarak[tetangga]:
                        jarak[tetangga] = jarak_baru
                        heapq.heappush(pq, (jarak_baru, tetangga))
        return jarak
    



graph = Graph()

print('SISTEM NAVIGASI LOGISTIK "KILAT MAJU"')
print("=========================================")

graph.tambah_jalan("Jakarta", "Bandung", 150)
graph.tambah_jalan("Jakarta", "Cirebon", 200)
graph.tambah_jalan("Bandung", "Tasikmalaya", 100)
graph.tambah_jalan("Bandung", "Cirebon", 130)
graph.tambah_jalan("Cirebon", "Semarang", 250)
graph.tambah_jalan("Tasikmalaya", "Semarang", 200)

graph.tampilkan_graph()

hasil = graph.graph_dijkstra("Jakarta")
print("\n[HASIL] Jarak Terpendek dari Jakarta:")
nomor = 1
for kota, jarak in hasil.items():
    if kota != "Jakarta":
        print(f"{nomor}. Ke {kota}: {jarak} km")
        nomor += 1
        
print("=========================================")
print("Simulasi Navigasi Selesai!")
