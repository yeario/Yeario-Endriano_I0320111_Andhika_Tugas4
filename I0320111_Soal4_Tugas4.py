print("Silahkan isi form berikut untuk melanjutkan")


usia = 21
kualifikasi = "Y"
usia = int(input("Masukan Usia Mu: "))
kualifikasi = input("Apakah anda sudah melalui kualifikasi? (Y/T): ")
if usia >= 21 and kualifikasi.upper() == "Y" :
    print("Kamu dapat mendaftar kursus")
else :
    print("Kamu tidak dapat daftar di kursus")