
import re as regex

print("Buatlah Fungsi Yang Dapat Digunakan Untuk Melakukan "
      "Pencarian Dari Sebuah String\n\n"
      "Contoh :\n"
      "Masukan String : <input>\n"
      "Cari Huruf     : <input>\n"
      "Hasil : Ditemukan <output> Huruf <output>\n\n")


str1 = input('Masukan String : ')
str2 = input('Cari Huruf     : ')
x = regex.findall(str2,str1)
print()
print('Hasil : Ditemukan',len(x),'Huruf',str2)
