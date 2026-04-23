# main.py - Menggunakan module keuangan.py
import keuangan

harga_barang = 1_000_000
ppn = keuangan.hitung_ppn(harga_barang)
total = harga_barang + ppn

print(f'Harga : {keuangan.format_rupiah(harga_barang)}')
print(f'PPN 11% : {keuangan.format_rupiah(ppn)}')
print(f'Total : {keuangan.format_rupiah(total)}')