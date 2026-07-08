print ("hello world")
print ("halo dunia")
print ("2030")

print ("indonesia")
# ini adalah comment
a = 10 #  ini adalah komen juga
""""ada apa yaa disni
semoga bisa konsisten di python
ini comment multi line -2026 juni 1"""
print (a)
# kita bisa mengcompiled python
# ke yang namanya bytecode
# cara mengcompile, buka terminal dan tuliskan 
# python -m py_compile main.py

# variabel adalah tempat menyimpan data

# manearu / assigment nilai

a = 10
x = 2
pendek = 100

#pemanggilan pertama
print ("nilai a =", a)
print ("nilai x =", x)
print ("nilai pendek =", pendek)

# penamaan 
nilai_y = 20 #menggunakan underscor
juta10 = 10000000 # angka gabole di depan
nilaiZ = 22

#pemanggilan kedua
print ("nilai a =", a)
a = 7
print ("nilai a =", a)

# assigmnet indirect
b = a
print ("nilai b =", b)

# a= 10, a adalah variabel yang bernilai 10

# tipe data : angka satuan (integer)
data_integer = 1
print ("data :" , data_integer)
print ("- bertipe :", type(data_integer))


# a= 10, a adalah variabel yang bernilai 10

# tipe data : angka satuan yang gada komanya (integer)
data_integer = 1
print ("data :" , data_integer)
print ("- bertipe :", type(data_integer))

# tipe data : angka dengann koma (float)
data_float  = 1.5
print ("data :" , data_float)
print ("- bertipe :", type(data_float))

# tipe data : kumpulan karakter (string)
data_string  = "ucup"
print ("data :" , data_string)
print ("- bertipe :", type(data_string))

# tipe data : biner true/false (boolean)
data_boolean  = True
print ("data :" , data_boolean)
print ("- bertipe :", type(data_boolean))

# tipe data khusus 

# bilangan kompleks
data_complex = complex(5,6)
print ("data :" , data_complex)
print ("- bertipe :", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double
data_c_double = c_double (1.5)
print ("data :" , data_c_double)
print ("- bertipe :", type(data_c_double))


# belajar casting
# merubah daritipe ke tipe yang lain
# tipe data= int, float, str, bool

# INTEGER
print("====INTEGER====")
data_int = 10
print ("data :" , data_int, "bertipe", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int 0 
print ("data :" , data_float,"berripe", type(data_float))
print ("data :" , data_str, "bertipe", type(data_str))
print ("data :" , data_bool,"berripe", type(data_bool))

# FLOAT
print("====FLOAT====")
data_float = 9.5
print ("data :" , data_float, "bertipe", type(data_float))

data_int = int(data_float) # akan di bulatkan kebawah                      
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai int 0 
print ("data :" , data_int,"berripe", type(data_int))
print ("data :" , data_str, "bertipe", type(data_str))
print ("data :" , data_bool,"berripe", type(data_bool))

# BOOLEAN
print("====BOOLEAN====")
data_bool = True
print ("data :" , data_bool, "bertipe", type(data_bool))

data_int = int(data_bool) # akan di bulatkan kebawah                      
data_str = str(data_bool)
data_float = float(data_bool) # akan false jika nilai int 0 
print ("data :" , data_int,"berripe", type(data_int))
print ("data :" , data_str, "bertipe", type(data_str))
print ("data :" , data_float,"berripe", type(data_float))

# SRTING
print("====STRING====")
data_str = "10"
print ("data :" , data_str, "bertipe", type(data_str))

data_int = int(data_str) # string harus angka                  
data_bool = str(data_str) # false jika string kosong
data_float = float(data_str) # akan false jika nilai int 0 
print ("data :" , data_int,"berripe", type(data_int))
print ("data :" , data_bool, "bertipe", type(data_bool))
print ("data :" , data_float,"berripe", type(data_float))

# input user

# data yg dimasukan pasti string

data = input("masukan nama: ")
print ("data =", data, "type data= ", type(data))

# jika kita ingin mengambil data integer maka
angka = float(input("masukan angka: "))
angka = int(input("masukan angka: "))

print ("data =", angka, "type data= ", type(angka))

#bagaimana dengan boolean
biner = bool(int(input("masukan angka boolean: ")))
print ("data =", biner, "type data= ", type(biner))

# operasi aritmatika

a = 10
b = 3

# operasi tambah
hasil = a + b
print (a,"+", b, "=", hasil)

# operasi pengurangan
hasil = a - b
print (a,"-", b, "=", hasil)

# operasi perkalian
hasil = a * b
print (a,"*", b, "=", hasil)

# operasi pembagian
hasil = a / b
print (a,"/", b, "=", hasil)

# operasi eksponen( pangkat ) **
hasil = a ** b
print (a,"**", b, "=", hasil)

# operasi modulus (sisa) %
hasil = a % b
print (a,"%", b, "=", hasil)

# operasi floor division //
hasil = a // b
print (a,"/", b, "=", hasil)

# operasi priority,

x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y / z // x
print (x,'**',y,'*',z,'+',x,'/',y,'-',y,'/',z,'//',x, '= ',hasil)

# Latihan konversi satuan temperature

# program konversi celcius ke satuan lain
print ('\nPROGRAM KONVERSI SUHU\n')
celcius = float(input('masukan angka dalam celcius '))
print ('suhu adalah ', celcius, 'celcius')

# reamur
reamur = (4/5) * celcius
print ('suhu dalam reamur adalah ', reamur, 'reamur')
# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print ('suhu dalam fahrenheit adalah ', fahrenheit, 'fahrenheit')
# kelvin
kelvin = celcius + 273
print ('suhu dalam kelvin adalah ', kelvin, 'kelvin')

# membuat pr 

print ('\nPROGRAM KONVERSI FAHRENHEIT KE KELVIN\n')
fahrenheit = float(input('masukan angka fahreheit :'))
print ('suhu adalah ', fahrenheit, 'fahrenheit')

celcius = 9 / 5 * ( fahrenheit - 32 )
kelvin = celcius + 273
print ('suhu dalam kelvin ', kelvin, 'kelvin')

print ('\nPROGRAM KONVERSI KELVIN KE FAHRENHEIT\n')
kelvin2 = float(input('masukan angka kelvin :'))
print ('suhu adalah ', kelvin2, 'kelvin2')

celcius2 = kelvin2 - 273
fahrenhiet2 = ((9 / 5) * celcius2) + 32
print ('suhu dalam fahrenheit ', fahrenhiet2, 'fahrenheit')

# operasi komperasi

# setiap hasil dari komperasim adalah boolean (true or false)

# >,<,>=,<=,==,!=,is, is not

a = 5
b = 2

# lebih besar dari >
print('--------- LEBIH BESAR DARI (>)')
hasil = a > 4
print (a, '>', 4,'= ',hasil)
hasil = b > 4
print (b, '>', 4,'= ',hasil)
hasil = b > 2
print (b, '>', 2,'= ',hasil)

# KURANG dari <
print('--------- KURANG DARI (<)')
hasil = a < 4
print (a, '<', 4,'= ',hasil)
hasil = b < 4
print (b, '<', 4,'= ',hasil)
hasil = b < 2
print (b, '<', 2,'= ',hasil)

# lebih dari sama dengan >=
print('--------- LEBIH DARI SAMA DENGAN(>=)')
hasil = a >= 4
print (a, '>=', 4,'= ',hasil)
hasil = b >= 4
print (b, '>=', 4,'= ',hasil)
hasil = b >= 2
print (b, '>=', 2,'= ',hasil)

# kurang dari sama dengan <=
print('-------- KURANG DARI SAMA DENGAN(<=)')
hasil = a <= 4
print (a, '<=', 4,'= ',hasil)
hasil = b <= 4
print (b, '<=', 4,'= ',hasil)
hasil = b <= 2
print (b, '<=', 2,'= ',hasil)

# sama dengan ==
print('--------- SAMA DENGAN(==)')
hasil = a == 5
print (a, '==', 5,'= ',hasil)
hasil = b == 5
print (b, '==', 5,'= ',hasil)

# tidak sama dengan !=
print('--------- TIDAK SAMA DENGAN(!=)')
hasil = a != 5
print (a, '!=', 5,'= ',hasil)
hasil = b != 5
print (b, '!=', 5,'= ',hasil)

# 'is' sebagai  komparasi objek identity
print('--------- OBJEK IDENTITY (is)')
x = 5 # ini assignment membuat objek    
y = 5
print ('nilai x = ', x, 'id = ', (hex(id(x))))
print ('nilai y = ', y, 'id = ', (hex(id(y))))
hasil = x is y
print ('x is y =', hasil)

x = 5
y = 6
print ('nilai x = ', x, 'id = ', (hex(id(x))))
print ('nilai y = ', y, 'id = ', (hex(id(y))))
hasil = x is y
print ('x is y =', hasil)

print('--------- OBJEK IDENTITY (is not)')
x = 5 # ini assignment membuat objek    
y = 6
print ('nilai x = ', x, 'id = ', (hex(id(x))))
print ('nilai y = ', y, 'id = ', (hex(id(y))))
hasil = x is not y
print ('x is not y =', hasil)

# operasi logika atau boolean

# or, and, xor, not

print('====NOT====')
a = True
b = not a
print('data boolean =', a )
print('---------NOT')
print('data boolean =', b)

print('====OR====') # or jika salah satu true maka hasilnya akan true
a = True
c = True
b = a or c
print(a, ' or', b,'=', c )
a = True
c = False
b = a or c
print(a, ' or', b,'=', c )
a = False
c = False
b = a or c
print(a, 'or', b,'=', c )
a = False
c = True
b = a or c
print(a, 'or', b,'= ', c )

print('====AND====') # and jika salah satu false maka hasilnya akan false KECUALI FALSE AND FALSE
a = True
c = True
b = a and c
print(a, ' and', b,'=', c )
a = True
c = False
b = a and c
print(a, ' and', b,'=', c )
a = False
c = False
b = a and c
print(a, 'and', b,'=', c )
a = False
c = True
b = a and c
print(a, 'and', b,'= ', c )

print('====XOR====') # xor akan true jika hanya salah satu, sisanya false
a = True
c = True
b = a ^ c
print(a, ' xor', b,'=', c )
a = True
c = False
b = a ^ c
print(a, ' xor', b,'=', c )
a = False
c = False
b = a ^ c
print(a, 'xor', b,'=', c )
a = False
c = True
b = a ^ c
print(a, 'xor', b,'= ', c )

# latihan komparasi dan logika 

# membuat gabungan area rentang
#++++++3--------10+++++++

angka = float(input('masukan angka yang lebih kecil dari 3 atau lebih besar dari 10 : '))

# ++++3-----------
# memerisa angka kurang dari 3
lebihkecil = angka < 3
print ('lebih kecil dari 3  ', lebihkecil)

#--------------10++++++
# memeriksa angka lebih dari 10
lebihbesar = angka > 10
print ('lebih besar dari 10 ', lebihbesar)

# ++++++3----------10+++++++
hasil = lebihbesar or lebihkecil
print ('angka yang anda masukan : ', hasil)

# -------3+++++++10-------
# kasus irisan

angka = float(input('masukan angka yang lebih besar dari 3 dan lebih kecil dari 10 : '))

# -------3++++++++++
lebihbesar = angka > 3
print ('lebih besar dari 3 : ', lebihbesar)

# +++++++++++++10---------
lebihkecil = angka < 10
print ('lebih kecil dari 10 : ', lebihkecil)

# ---------3++++++10---------
hasil = lebihbesar and lebihkecil
print ('angka yang anda masukan : ', hasil)



# pr
data = float(input('masukan angka '))

p = data > 0 
print ('hasil dari proses ',p)

p2 = data < 5
print ('hasil dari proses2',p2)

p3 = data > 8   
print ('hasil dari proses3',p3)

p4 = data < 11
print ('hasil dari proses4',p4)

hasil = p and p2 or p3 and p4
print('hasil dari rentang dari program anda',hasil)

print('===================')

p = data < 0 
print ('hasil dari proses ',p)

p2 = data > 5
print ('hasil dari proses2',p2)

p3 = data < 8   
print ('hasil dari proses3',p3)

p4 = data > 11
print ('hasil dari proses4',p4)

hasil = p or p2 and p3 or p4
print('hasil dari rentang dari program anda',hasil)

# operator bitwise, operasi biner, binary

a = 9
b = 5
# bitwise OR (|)
print ('\n=======OR=======')
c = a | b
print ('nilai :', a, ' binary :', format(a,'08b'))
print ('nilai :', b, ' binary :', format(b,'08b'))
print ('--------------------------(|)')
print ('nilai :', c, 'binary :', format(c,'08b'))

# bitwise AND (&)
print ('\n=======AND=======')
c = a & b
print ('nilai :', a, ' binary :', format(a,'08b'))
print ('nilai :', b, ' binary :', format(b,'08b'))
print ('--------------------------(&)')
print ('nilai :', c, 'binary :', format(c,'08b'))

# bitwise XOR (^)
print ('\n=======XOR=======')
c = a ^ b
print ('nilai :', a, ' binary :', format(a,'08b'))
print ('nilai :', b, ' binary :', format(b,'08b'))
print ('--------------------------(^)')
print ('nilai :', c, 'binary :', format(c,'08b'))

# bitwise NOT (~)
c = ~a
print ('\n=======NOT=======')
print ('nilai :', a, ' binary :', format(a,'08b'))
print ('--------------------------(~)')
print ('nilai :', c, ' binary :', format(c,'08b'))
print ('--------------------------(^)')
d = 0b00001001
e = 0b11111111
print ('nilai :', e^d, ' binary :', format(e^d,'08b'))

# shifting

#shift right (>>)

c = a >> 1
print ('\n=======>>=======')
print ('nilai :', a, ' binary :', format(a,'08b'))
print ('--------------------------(>>)')
print ('nilai :', c, ' binary :', format(c,'08b'))

#shift left (<<)

c = a << 1
print ('\n=======<<=======')
print ('nilai :', a, ' binary :', format(a,'08b'))
print ('--------------------------(>>)')
print ('nilai :', c, ' binary :', format(c,'08b'))

# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a  = 5 # ini adalah assignment
print ('nilai a =',a)

a +=1 # artinya adalah a = a + 1
print ('nilai a += 1, nilai a menjadi',a)

a -=2 # artinya adalah a = a - 2
print ('nilai a -= 2, nilai a menjadi',a)

a *=5 # artinya adalah a = a * 5
print ('nilai a *= 5, nilai a menjadi',a)

a /=2 # artinya adalah a = a / 2
print ('nilai a /= 2, nilai a menjadi',a)

# modulus and floor divisoin
b = 10
print ('\nnilai b =',b)

b %= 3
print ('nilai b %= 3, nilai b menjadi',b)

b = 10
print ('\nnilai b =',b)

b //= 3
print ('nilai b //= 3, nilai b menjadi',b)

# pangkat / eksponen
a = 5
print ('\nnilai a =',a)

a **= 3
print ('nilai a **= 3, nilai a menjadi',a)

# operasi bitwise
# OR
c = True
print ('\nnilai c =',c)
c |= False
print ('nilai c |= false, nilai c menjadi',c)
c = False
print ('nilai c =',c)
c |= False
print ('nilai c |= false, nilai c menjadi',c)

# AND
c = True
print ('\nnilai c =',c)
c &= False
print ('nilai c &= false, nilai c menjadi',c)
c = True
print ('nilai c =',c)
c &= True
print ('nilai c &= true, nilai c menjadi',c)

# XOR
c = True
print ('\nnilai c =',c)
c ^= False
print ('nilai c ^= false, nilai c menjadi',c)
c = True
print ('nilai c =',c)
c ^= True
print ('nilai c ^= true, nilai c menjadi',c)

# geser geser
d = 0b0100
print ('\nnilai d =',format(d,'04b'))
d >>= 2
print ('nilai d >>= 2, nilai d menjadi',format(d,'04b'))
d <<= 1
print ('nilai d <<= 1, nilai d menjadi',format(d,'04b'))


data = 'ini adalah string'
print(data)
print(type(data))

# 1. cara membuat string

'''
      1. menggunakan single quote '...'
      2. menggunakan double quote "..."
'''

data = ' mengunakan singgle quote'
print(data)

data = " mengunakan singgle quote"
print(data)

print('"halo, apakabar?"')
print("'halo, apakabar?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('ini juga hari jum\'at')
print('g\'day, isn\'t it?')

# backslash
print('C:\\users\\on')

# tab
print('aku\tkamu, jadi jauhan:(')

# backspace
print('aku \bkamu, jadi deket:)')

# new line
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR carrieage return -> acorn, commodore, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> carriage return line feed -> windows

# 3. string literal atau raw
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new \b\n\r\\folder') # jika dikasi r maka semuanya menjadi string

# multiline literal string
print("""
    Nama : joko
    Kelas : 9  
""")

# multiline sring literal and raw
print(r"""
    Nama : joko
    Kelas : 9 sd\new 
    website : www.joki.com/newID  
""")
\
# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = 'yves'
nama_kedua = 'De'
nama_ketiga = 'laurent'

nama_lengkap = nama_pertama + ' ' + nama_kedua + "'" + nama_ketiga
print(nama_lengkap)

# 2. menhitung panjang dari string
panjang = len(nama_lengkap)
print('panjang dari ' + nama_lengkap + '=' + str(panjang)) 

# 3. mengecek apakah ada char atau string di dalam string
d = 'd'
status = d in nama_lengkap
print ( d + ' ada di ' + nama_lengkap + '=' + str(status))

D = 'D'
status = D in nama_lengkap
print ( D + ' ada di ' + nama_lengkap + '=' + str(status))

d = 'd'
status = d not in nama_lengkap
print ( d + ' tidak ada di ' + nama_lengkap + '=' + str(status))

# mengulang string
print('AH'*10)
print(15*'AKU ')

# indexing
print('index ke-0 ' + nama_lengkap[0])
print('index ke-7 ' + nama_lengkap[7])
print('index ke-(-3) ' + nama_lengkap[-3])
print('index ke-(0:4) ' + nama_lengkap[0:5])
print('index ke-(0:15) ' + nama_lengkap[0:16])
print('index ke-(0,2,4,6,8,10) ' + nama_lengkap[0:10:2])

# item paling kecil
print('item paling kecil ' + min(nama_lengkap))
# item paling besar
print('item paling besar ' + max(nama_lengkap))

ascii_code = ord(' ')
print('ascii code untuk space : ' + str(ascii_code))
data = 111
print('char untuk ascii 111 adalah ' + chr(data))

# 4. operator dalam bentuk method
data = ('jasa jisi jusu jese')
jumlah = data.count('j')
print ('jumlah j pada ' + data + ' = ' + str(jumlah))

#operator dalam bentuk method

## mengubah case dari string

# merubah semua ke upper case

salam = 'bro!'
print('normal :', salam)
salam = salam.upper()
print('upper  :', salam)

# merubah semua ke lower case
alay = 'aKu Keren gAk sIeeeEEEEeeeeeeEe'
print('normal :',alay)
alay = alay.lower()
print('lower :', alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = 'sist'
lower = salam.islower() # hasilnya bool
print (salam, ' is lower :', str(lower))
upper = salam.isupper()
print (salam, ' is upper :', str(upper))

# isalpha() -> untuk mnegecek jika semua huruf tidak kosong
# isalnum() -> cek huruf dan angka
# isdecimal() -> cek angka saja
# isspace() -> spasi, tab, newline, \n
# istitle() -> semua kata dimulai dengan huruf besar

judul = 'Beeing Rich Just Play A Number Game'
cek_judul = judul.istitle() # hasil bool

print (judul, 'is title :', str(cek_judul))

# ngecek komponen startswith() and endswith()
cek_start = 'Kimyangsuk Dejonh'. startswith('Kimyangsuk')
print ('start :',str(cek_start))

cek_end = 'Kimyangsuk Dejonh'.endswith('Dejonh')
print ('end :',str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ' '.join(pisah)
print (gabungan)
gabungan = 'akuehmsayangehmkamu'
print (gabungan.split('ehm'))

# alokasi kkarakter rjust(), ljust(), center()
kanan = 'kanan'.rjust(10)
print ("'",kanan,"'")

kiri = 'kiri'.ljust(10)
print ("'",kiri,"'")

tengah = 'tengah'.center(20,'-')
print ("'",tengah,"'")

# kebalikanya strip()
tengah = tengah.strip('-') # menghilangkan tanda -
print ("'",tengah,"'")

# format string

# contoh generic
# string
nama = 'rafi '
format_str = f"hello {nama}"
print (format_str)

# bool
boolean = True
format_str = f"boolean : {boolean}"
print(format_str)

# angka
angka = 15.11
format_str = f"angka anda : {angka}"
print(format_str)

# bilangan bulat
angka = 16
format_str = f"bilangan bulat : {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
ribuan = 1234
format_str = f"ribuan : {ribuan:,}"
print(format_str)

# angka desimal
angka = 83.8012345
format_str = f"angka desimal : {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 83.8012345
format_str = f"angka desimal : {angka:06.2f}"
print(format_str)

# menampilkan tana + atau -
angka_minus = -16
angka_plus = 16.12345
format_minus = f"minus : {angka_minus:+d}"
format_plus = f"plus : {angka_plus:+.3f}"

print (format_minus)
print (format_plus)

# memformat persen
presentase = 0.0070
format_str = f"presentase : {presentase:.2%}"
print(format_str)

# melakukan operasi di dalam placeholder
harga = 111111
jumlah_barang = 7
format_str = f"harga total : Rp.{harga*jumlah_barang:,}"
print(format_str)

# format untuk angka lain
angka = 255
format_binary = f"binary : {bin(angka)})"
format_octal = f"octal : {oct(angka)})"
format_hex = f"hex : {hex(angka)})"

print (format_binary)
print (format_octal)
print (format_hex)

# width and multiline

# data

nama = 'yves laurent'
umur = 16
tinggi  = 173
uk_sepatu = 43

# string biasa
data = f"Nama : {nama} Umur : {umur} Tinggi : {tinggi} uk Sepatu : {uk_sepatu}"
p = 'data'.center(20,'-')
print ('\n',p)
print (data)

# string multiline ( menggunakan enter, newline, \n)
data = f"Nama : {nama} \nUmur : {umur} \nTinggi : {tinggi} \nuk Sepatu : {uk_sepatu}"
p = 'data'.center(20,'-')
print ('\n',p)
print (data)

# string multiline (kutip triplet)
data = f"""Nama = {nama}
Umur = {umur}
Tinggi = {tinggi}
Uk sepatu = {uk_sepatu}
"""
p = 'data'.center(20,'-')
print ('\n',p)
print (data)

# mengatur lebar
nama = 'yves'
data = f"""
Nama      = {nama:>5}
Umur      = {umur:>5}
Tinggi    = {tinggi:>5}
Uk sepatu = {uk_sepatu:>5}
"""
p = 'data'.center(20,'-')
print ('\n',p)
print (data)

# if dan else statement

# 1. if nya
# 2. kondisi
# 3. aksi

nama = input('masukan nama anda : ')

# program sebelumnya
# if kondisi : aksi
# program selanjutnya

# 1. program if inlie
if nama=='yves' : print ('selamat datang bos besarr')
print (f'terima kasih telah \nmenghubungi kami -{nama}')

# 2. program if dengan indentation

if nama=='yves':
    print('selamat datang kembali')
    print('ada yang bisa di bantu?',nama)
print (f'terima kasih telah \nmenghubungi kami -{nama}')

# 3. else statement

if nama=='rafi':
    print('eh haii selamat yaa masuk \nsman 6 semarang')
    print('tetep sama aku ya -python')
else:
    print('eh siapa ini')
    print('mohon maaf saya tidak kenal')
print (f'terima kasih telah \nmenghubungi kami -{nama}')

# ELIF =  else if statement

nama = input('nama kamu siapa? ')

if nama=='rafi':
    print('hai bosss')
elif nama=='milo':
    print('haii kingg!!!!')
else : print ('maaf anda siapa yaa?')
print ('end of program')

# perulangan (loop)

# for  kondisi:
#     aksi

# ini dengan list
angka = [0,1,2,3,4] # ini list
print(angka)

for i in angka:
    print(f'i sekarang -> {i}')
print('end\n')

# ini  dengan range
angka2 = range(7)

for i in range(7):
    print (f'i sekarang -> {i}')
print('end 2\n')

angka2 = range(1,7)

for i in range(1,7):
    print (f'i sekarang -> {i}')
print('end 3\n')

# menggunakan string

data = 'hai future'

for huruf in data:
    print(huruf)

# while loop

# while kondisi:
#    aksi ini
#    aksi itu

# akhir dari program

angka = 0
print(f'angka sekarang -> {angka}')

while angka < 7:
    angka += 1
    print(f'angka sekarang -> {angka}')
    print('haii bos besarrrr')

print ('cukupppp')

# countiue, pass, and break

# pass -> berfungsi sebagai dummy, tidak akan di eksekusi

angka = 0

while angka < 4:
    if angka == 3:
        pass #
        

    angka += 1
    print(angka)

# countinue


angka = 0
print(f'angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print (f'angka sekarang -> {angka}')

    if angka == 3:
        print ('oalahhh')
        continue # akan membuat loop meloncat ke step selanjutnya


    print ('CUKUPPPP')

# break
print('\n========================\n')
#  contoh 1
angka = 0

while angka < 7:
    angka += 1
    print(f'angka sekarang -> {angka}')
    if angka == 4:
        print('sudah sampai')
        break    
    print('iyaa')

print('cukuppp sudahh')

# contoh 2
data = int(input('hitung sampai : '))

angka = 0

while True:
    angka += 1
    print(f'count = {angka}')
    if angka == data:
        print('sudah sampai')
        break    
    print('iyaa')

print('cukuppp sudahh')

# latihan perulangan membuat segitiga

sisi = 7

# 1. menggunakan for

# dummy variable
print('=====for=====')
count = 1
for i in range(sisi):
    print('*'*count)
    count+=1


# 2. mengunakan while
print('=====while=====')
count = 1
while True:
    print('*'*count)
    count+=1

    if count > sisi:
        break

# 3. hanya ganjil saja
print('===============')
count = 1
while True:
    if (count%2):
        # print jika ganjil
        print('*'*count)
        count+=1
    else:
        # akan kembali ke atas jika ganjil
        count+=1
        continue

    if count > sisi:
        # akan break jika melebihi sisi
        break


# 4. hanya ganjil saja
print('===============')
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(' '*spasi,'+'*count)
        spasi -= 1
        count+=1
    else:
        count+=1
        continue

    if count > sisi:
        break

# list 

# kumpulan data numbers
angka = [1,2,3,4,1]
print(angka)

# kumpulan data string
data = ['yves', 'de', 'laurent']
print(data)

# kumpulan data boolean
boolean = [True,False,False,True]
print(boolean)

# kumpulan campuran
campuran = [1,'yves',True]
print(campuran)

# cara alternatif membuat list
jarak = range(0,7,2)# range(start,stop,step)
print(jarak)
listing = list(jarak)
print(listing)

# membuat list dari for loop, list comperhension
pake_for = [i*2 for i in range(0,7)]
print (pake_for)

# membuat list pake for and if
pake_if_juga = [i for i in range(0,10) if i != 5]
print (pake_if_juga)

pake_if_juga = [i**2 for i in range(0,10) if i%2 ==0]
print(pake_if_juga)

pake_if_juga = [i**1 for i in range(0,10) if i%2 ==1]
print(pake_if_juga)

   # operasi

# indeks   0(-3) 1(-2)  2(-1)
data = ['yves','de','lauret']

# mengambil data dari list ini
data_1 = data[1]
print('data pertama (indeks)', data_1)

data_3 = data[-1]
print('data terakhir (indeks)', data_3)

data_yves = data[-3]
print(f'data yves -> {data_yves}')

# mengambil info data dari list

panjang = len(data)
print(f'panjang data = {panjang}')

# manipulasi data list

# menambah item pada list sesuai posisi
print(f'data sebelum ditambah = \n{data}')

data.insert(2,'jonh')
print(f'data setelah ditambah = \n{data}')

# menambah data di akhir list
data.append('karamoy')
print(f'data setelah ditambah lagi = \n{data}')

# menambah list dengan list
data_baru = ['dj','panduy','rimexxx']
data.extend(data_baru)
print(f'data gabungan = \n{data}')

# merubah data
# merubah data 2 menjadi klakson
data[2] = 'klakson'
print(f'data yang di ganti = \n{data}')

# meremove data

data.remove('de')
print(f'data remove = \n{data}')
# data.remove('Yves") akan eror karena huruf nya tidak sesuai yaitu 'yves'

# meremove data paling belakang
data_akhir = data.pop()
print(f'data akhir = \n{data}')

print(data_akhir)

data_angka = [1,3,5,6,8,7,4,3,5,7,9,1,5,8,9]

print(f'data angka = \n{data_angka}')

# count data

jumlah7 = data_angka.count(7)
jumlah4 = data_angka.count(4)

print(f'jumlah data 7 = {jumlah7}')
print(f'jumlah data 4 = {jumlah4}')

# ambil posisi data (index)

data = ['michael','de','klakson','rimexx']

print(f'data = {data}')

michael = data.index('michael')
klakson = data.index('klakson')

print(f'index michael = {michael}')
print(f'index klakson = {klakson}')

# mengurutkan list 

print(f'data angka sebeluum di sort = \n{data_angka}')
data_angka.sort()
print(f'data angka sort = \n {data_angka}')

print(f'data = {data}')
data.sort()
print(f'data sort = {data}')

# balik list
data_angka.reverse()
data.reverse()
print(f'data di reverse \n{data_angka}\n{data}')

# teknik menduplikat data/list

a = ['michael','de','klakson']
print(f'a = {a}')

b = a # pass by reference
print(f'b = {b}')

# kita akan merubah memberr dari a

# ini akan merubah semua list
a[1] = 'lev'
b.sort()
print(f'a = {a}')
print(f'b = {b}')

# address dari kedua list a dan b
print(f'addres a = {hex(id(a))}')
print(f'addres b = {hex(id(b))}')

# menduplikat data menggunakan copy

print('membuat list c mengunakan a.copy()')
c = a.copy() # full duplikat / data baru 

print(f'addres a = {hex(id(a))}')
print(f'addres b = {hex(id(b))}')
print(f'addres c = {hex(id(c))}')

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print('\nkita rubah data 1')
c[1] = 'liv'

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print('\nkita rubah data 0')
a[0] = 'kliksin'

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

# nested list
data_1 = [1,2,3]
data_2 = [0,9,8]

data_biasa = [1,2,3,0,9,8]

print(f'data list biasaa {data_biasa}')

list_gabungan = [data_2,data_1,]
print(f'data gabungan {list_gabungan}\t')

# contoh penggunaan

p1=['michael',21,'laki-laki']
p2=['jina',67,'wanita']
p3=['klakson',11,'laki-laki']

p_semua=[p1,p2,p3]

print(f'smeua p {p_semua}')

for p in p_semua:
    print(f'nama \t\t-> \t{p[0]}')
    print(f'umur \t\t-> \t{p[1]}')
    print(f'kelamin \t-> \t{p[2]}\n')

p_copy = p_semua.copy()
print(f'peserta = {p_copy}')
p1[0] = 'jekson'
print(f'peserta = {p1}')
print(f'peserta = {p_copy}')

# deep copy list nested

data_1 = [1,2,3]
data_2 = [0,9,8]

data_biasa = [1,2,3,0,9,8]

p_semua = [data_1,data_2,9]

print('\n======================')
p_semua_copy = p_semua.copy()
print(f'\ndata = {p_semua}')
print(f'\ndata = {p_semua_copy}')

# menganmbil data nested list
data=p_semua[0][0]
print(f'\ndata = {data}')

# addres semuanya
print(f'address asli = {hex(id(p_semua))}')
print(f'address copy = {hex(id(p_semua_copy))}')

print('\naddress dari member ke-1')
print(f'address asli = {hex(id(p_semua[0]))}')
print(f'address copy = {hex(id(p_semua_copy[0]))}')

p_semua[0][1]=7
p_semua[2]=7
print(f'address asli = {p_semua}')
print(f'address copy = {p_semua_copy}')

# kita gunakan deepcopy
from copy import deepcopy
p_semua = [data_1,data_2,9]
p_deepcopy = deepcopy(p_semua)

print(f'\naddress asli = {hex(id(p_semua))}')
print(f'address deepcopy = {hex(id(p_deepcopy))}')


print('address dari member ke-1')
print(f'address asli = {hex(id(p_semua[0]))}')
print(f'address deepcopy = {hex(id(p_deepcopy[0]))}')

p_semua[0][0]=99
print(f'address asli = {hex(id(p_semua[0]))}')
print(f'address copy = {hex(id(p_semua_copy[0]))}')
print(f'address deepcopy = {hex(id(p_deepcopy[0]))}')