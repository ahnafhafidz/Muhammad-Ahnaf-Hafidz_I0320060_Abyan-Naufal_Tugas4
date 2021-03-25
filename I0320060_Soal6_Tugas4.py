#Soal 6

x = 4
y = 11

print("x = ", x, ",Mempunyai nilai biner: ", format(x,"08b"))
print("y = ", y, ",Mempunyai nilai biner: ", format(y,"08b"))

a = x|y
print("a. Hasil dari 4 | 11 adalah: ", a, ", Nilai binernya: ", format(a,"08b"))

b = x>>y
print("b. Hasil dari 4 >> 11 adalah: ", b, ", Nilai binernya: ", format(b,"08b"))

c = x^y
print("c. Hasil dari 4^11 adalah: ", c, ", Nilai binernya: ", format(b,"08b"))

d = ~x
print("d. Hasil dari ~4 adalah: ", d, ", Nilai binernya: ", format(d,"08b"))

e = y&x
print("e. Hasil dari 11 & 4 adalah: ", e, ", Nilai binernya: ", format(e,"08b"))