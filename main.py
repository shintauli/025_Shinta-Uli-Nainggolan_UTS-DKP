# UTS Dasar Komputer dan Pemrograman - Kelompok F
# Pengelompokan nilai mahasiswa

data_inti = [42, 55, 61, 68, 73, 79, 82, 87, 91, 64, 58, 76, 84, 49, 95]
data_tambahan = [59, 60, 79, 80, 100]
data_nilai = data_inti + data_tambahan


def kategori(nilai):
    if nilai < 60:
        return "RENDAH"
    elif nilai < 80:
        return "SEDANG"
    else:
        return "TINGGI"


def rata_rata(data):
    return sum(data) / len(data)


def hitung_kategori(data):
    jumlah = {"RENDAH": 0, "SEDANG": 0, "TINGGI": 0}
    for nilai in data:
        jumlah[kategori(nilai)] += 1
    return jumlah


def main():
    print("=" * 40)
    print(" PENGELOMPOKAN NILAI MAHASISWA")
    print("=" * 40)

    print("\n--- DATA MASUK (INPUT) ---")
    print("Data inti     :", data_inti)
    print("Data tambahan :", data_tambahan)
    print("Jumlah data   :", len(data_nilai))

    print("\n--- PENGOLAHAN NILAI (PROSES) ---")
    nomor = 1
    for nilai in data_nilai:
        print(f"{nomor:02d}. Nilai = {nilai} -> {kategori(nilai)}")
        nomor += 1

    jumlah = hitung_kategori(data_nilai)

    print("\n--- HASIL AKHIR (OUTPUT) ---")
    print("Total data      :", len(data_nilai))
    print("Jumlah RENDAH   :", jumlah["RENDAH"])
    print("Jumlah SEDANG   :", jumlah["SEDANG"])
    print("Jumlah TINGGI   :", jumlah["TINGGI"])
    print(f"Rata-rata       : {rata_rata(data_nilai):.2f}")
    print("Nilai tertinggi :", max(data_nilai))
    print("Nilai terendah  :", min(data_nilai))
    print("=" * 40)
    print(" PEMROSESAN SELESAI")
    print("=" * 40)


if __name__ == "__main__":
    main()