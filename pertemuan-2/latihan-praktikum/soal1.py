stok = [15, 50, 30, 25, 40]

stok.append(100)

stok.insert(2, 75)

stok.sort(reverse = True)

total = stok[0] + stok[1] + stok[2] + stok[3] + stok[4] + stok[5] + stok[6]
average = total / 7
print(f"Rata-rata = {average}")

print(stok)