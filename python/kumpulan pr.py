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

# date and time (latihan)

import datetime as dt

today = dt.date.today()
print (today)
print (f"hari ini hari : {today:%A}")

month = dt.date(2020,1,1)
print (month)
print (f"hari ini hari : {month:%A}")

print ('masukan tanggal, bulan, dan tahun lahir anda')
tanggal = int(input('tanggal \t:'))
bulan = int(input('bulan \t\t:'))
tahun = int(input('tahun \t\t:'))

lahiran = dt.date(tahun, bulan, tanggal)
print (f"tanggal lahir sand adalah : {lahiran}")

today = dt.date.today()
umur_hari = today - lahiran
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print (f" hari ini tanggal : {today}")
print (f"hari lahir anda adalah : {lahiran:%A}")
print (f"umur anda sekarang : {umur_tahun} tahun {umur_bulan_sisa} bulan")

# latihan kalkulator sederhana

print('='*20)
print('kalkulator sederhana')
print('='*20)

pw = input('masukan password : ')
if pw=='milo':
    print ('selamat datang di kalkulator')
else: print('password salah !!'),


angka_1 = float(input('masukan angka : '))
operator = (input('operator (+,-,x,/) : '))
angka_2 = float(input('masukan angka lagi : '))

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == 'x' or operator == 'x':
    hasil = angka_1 * angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah = {hasil}')
else:
    print('masukin operatornya yang bener dong!!')
print('end progarm')

# latihan perulangan membuat ketupat

sisi = 5
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
sisi = 2
count = 3
spasi = int(sisi/2)
while True:
    if (count%2):
        print(' '*spasi,'+'*count)
        spasi += 1
        count-=1
    else:
        count-=1
        continue

    if count == 0:
        break