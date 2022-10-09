# program menghitung nilai mahasiswa

print('\nProgram Python Menghitung Nilai Mahasiswa\n')
NIM = input('Masukan NIM Anda : ')
Nama = input('Masukan Nama Anda : ')
Gender = input('Gender : ')
TanggalInputNilai = input ('Tanggal Input Nilai : ')
Matakuliah = input ('Masukan Mata Kuliah : ')
Absen = float(input('Masukan Nilai Absensi : '))
Tugas = float(input('Masukan Nilai Tugas :'))
UTS = float(input('Masukan Nilai UTS :'))
UAS = float(input('Masukan Nilai UAS :'))

R_Absen = int(Absen * 20/100)
R_Tugas = int(Tugas * 25/100)
R_UTS = int(UTS * 25/100)
R_UAS = int(UAS * 30/100)

Nilai_Akhir =R_Absen+R_Tugas+R_UTS+R_UAS

print('Nilai Akhir')
print('Tanggal Input Nilai:'+TanggalInputNilai)
print('Nama :'+Nama)
print('NIM :'+NIM)
print('MataKuliah'+Matakuliah)
print('Nilai_Akhir',int(Nilai_Akhir))

if Nilai_Akhir >= 80:
    print('Grade : A')
elif Nilai_Akhir >= 77:
    print('Grade : A-')
elif Nilai_Akhir >= 74:
    print('Grade : B+')
elif Nilai_Akhir >= 71:
    print('Grade : B')
elif Nilai_Akhir >= 68:
    print('Grade : B-')
elif Nilai_Akhir >= 64:
    print('Grade : C+')
elif Nilai_Akhir >= 60:
    print('Grade : C')
elif Nilai_Akhir >= 50:
    print('Grade : D')
elif Nilai_Akhir >= 0:
    print('Grade : E')

if Nilai_Akhir >= 60:
    print ('Keterangan : Lulus')
else:
    print('Keterangan : Tidak Lulus')
