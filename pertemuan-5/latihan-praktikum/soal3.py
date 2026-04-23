"""
Terdapat dua data pendaftar UKM (Unit Kegiatan Mahasiswa): 
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
a. Tampilkan mahasiswa yang hanya mendaftar di ukm_coding saja (tidak mendaftar di 
robotik).
b. Tampilkan daftar seluruh mahasiswa unik yang mendaftar di salah satu atau kedua 
UKM tersebut.
c. Cek apakah "Andi" merupakan anggota dari ukm_robotik. Tampilkan hasil dalam 
bentuk boolean.
"""

ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

hanya_ukm_coding = ukm_coding - ukm_robotik
print(hanya_ukm_coding)

semua = ukm_coding | ukm_robotik
print(semua)

print("Andi" in  ukm_robotik)