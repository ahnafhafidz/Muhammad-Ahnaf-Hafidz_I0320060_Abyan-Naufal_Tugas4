#Soal 4

#input persyaratan
print("Berapa Usia Kamu ?")
usia = int(input("Usia: "))

print("Apakah anda sudah lulus ujian kualifikasi ?")
lulus = input("Lulus: ")

if usia >= 21:
    if lulus == 'Y':
        print("Anda dapat mendaftar di kursus")
    else:
        print("Anda tidak dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")