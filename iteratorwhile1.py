angka = 1
str1 = 'Nomor absen '
str2 = ' Pulang aja'

while angka <=10:
   angka += 1
   #print(str1 + str(angka) + str2)
   #print("%s%s%s" % (str1, angka, str2))
   print("{}{}{}".format(str1, angka, str2))
