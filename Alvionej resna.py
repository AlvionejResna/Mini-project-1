print("data diri")

nama=input("masukkan nama : ")
nim=input("masukkan nim : ")
kelas=input("masukkan kelas : ")
program_studi=input("masukkan program_studi : ")

print('#program menghitung gaji karyawan')
print('=================================')

while True:
    jam_kerja=int(input("masukkan jam kerja : "))
    tarif_kerja=int(input("masukkan tarif kerja  : "))

    if (jam_kerja > 160):
        tarif_bonus = float(tarif_kerja + (tarif_kerja * 0.1))
        print("tarif asli :", tarif_kerja)
        print("tarif dengan bonus :", tarif_bonus)
    else:
        print("tarif asli :", tarif_kerja)
        print("tidak ada bonus")

    keluar=input("apakah ingin keluar dari program? (Yes/No): ")
    if keluar == "Yes":
        print("terima kasih telah menggunakan program ini")
        break
    