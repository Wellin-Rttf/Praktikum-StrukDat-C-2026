from kurs import kurs

def konversi(dari, ke, jumlah):
    try:
        if dari == "IDR":
            return jumlah / kurs[ke] if ke != "IDR" else jumlah
        elif ke == "IDR":
            return jumlah * kurs[dari]
        else:
            return (jumlah * kurs[dari]) / kurs[ke]
    except:
        if dari not in kurs and dari != "IDR":
            raise ValueError("Kode mata uang tidak valid!")
        elif ke not in kurs and ke != "IDR":
            raise ValueError("Kode mata uang tidak valid!")