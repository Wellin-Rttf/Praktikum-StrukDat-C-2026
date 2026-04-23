# keuangan.py - Module untuk perhitungan keuangan sederhana
def hitung_ppn(harga, persen=11):
    """Menghitung PPN dari harga."""
    ppn = harga * (persen / 100)
    return ppn

def format_rupiah(jumlah):
    """Memformat angka ke format Rupiah."""
    return f'Rp {jumlah:,.0f}'.replace(',', '.')

def hitung_cicilan(pokok, bunga_persen, bulan):
    """Menghitung cicilan per bulan (bunga flat)."""
    total_bunga = pokok * (bunga_persen / 100) * (bulan / 12)
    return (pokok + total_bunga) / bulan