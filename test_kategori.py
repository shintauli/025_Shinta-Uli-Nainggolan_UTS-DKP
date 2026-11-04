from main import kategori

# (nilai uji, hasil yang diharapkan menurut aturan soal)
data_uji = [
    (45, "RENDAH"),   # nilai rendah realistis
    (59, "RENDAH"),   # 1 di bawah batas 60
    (60, "SEDANG"),   # tepat di batas 60
    (61, "SEDANG"),   # 1 di atas batas 60
    (79, "SEDANG"),   # 1 di bawah batas 80
    (80, "TINGGI"),   # tepat di batas 80
    (81, "TINGGI"),   # 1 di atas batas 80
    (92, "TINGGI"),   # nilai tinggi realistis
]

print("=" * 65)
print(" PENGUJIAN FUNCTION kategori()")
print("=" * 65)

jumlah_pass = 0
nomor = 1
for nilai, expected in data_uji:
    actual = kategori(nilai)
    if actual == expected:
        hasil = "PASS"
        jumlah_pass += 1
    else:
        hasil = "FAIL"
    print(f"Test {nomor} | Input = {nilai:>3} | Expected = {expected:<6} | Actual = {actual:<6} | {hasil}")
    nomor += 1

print("-" * 65)
print(f"Hasil: {jumlah_pass} dari {len(data_uji)} test PASS")