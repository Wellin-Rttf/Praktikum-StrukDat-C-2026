from tabulate import tabulate
from kurs import kurs
from konverter import konversi

print("=== KONVERTER MATA UANG ===")
print(tabulate(kurs.items(), headers=["Kode", "Kurs"], tablefmt="outline"))

dari = input(f"Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke   = input(f"Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

hasil = konversi(dari, ke, jumlah)

if dari == "IDR":
    print(f"Rp{jumlah:.0f} = {hasil:.2f} {ke}")
elif ke == "IDR":
    print(f"{jumlah:.2f} {dari} = Rp{hasil:.0f}")
else:
    print(f"{jumlah:.0f} {dari} = {hasil} {ke}")
