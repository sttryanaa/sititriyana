print('PENDONOR DARAH')

nama_pendonor = str(input('Masukkan Nama :'))
usia = int(input('Masukkan Usia :'))
berat_badan = float(input('Masukkan Berat Badan Anda :'))
kondisi = str(input('Apakah kondisi Anda sehat? (ya/tidak) :'))
hamil = str(input('Apakah Anda dalam kondisi hamil? (ya/tidak) :'))
menyusui = str(input('Apakah Anda sedang dalam menyusui? (ya/tidak) :'))
konsumsi_alkohol = str(input('Apakah Anda konsumsi alkohol dalam 48 jam terakhir? (ya/tidak) :'))
penyakit_menular = str(input('Apakah Anda memiliki penyakit menular? (ya/tidak) :'))

if usia > 17 and berat_badan > 45 and kondisi == 'ya' and hamil == 'tidak' and menyusui == 'tidak' and konsumsi_alkohol == 'tidak' and penyakit_menular == 'tidak' :
    status = 'Silahkan Mendonorkan Darah Anda'
else:
    status = 'Mohon Maaf, Anda Belum Memenuhi Syarat Untuk Menjadi Pendonor'
print(status)
print('Terimakasih')

