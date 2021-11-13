#praktikum_metnum Ricky Suryanto Parsaulian Samosir 202010225254 TF3A6

#interpolasi lagrange

import numpy as np

#Membaca Jumlah titik data
print ()
n = int(input('Masukkan jumlah titik data: '))

# Membuat array ukuran n x n dan inist.
x = np.zeros((n))
y = np.zeros((n))

# Membaca titik data
print ()
print('Masukkan data x dan y: ')
print ()
for i in range(n):
  x[i] = float(input( 'x[' +str(i)+ ']='))
  y[i] = float(input( 'y[' +str(i)+ ']='))

#Membaca Interpolasi titik
print ()
xp = float(input('Masukkan x yang diinginkan: '))

#Inisiasi interpolasi
yp = 0

# Implementasi Interpolasi Lagrange
for i in range(n):

  p = 1

  for j in range(n):
    if i != j:
      p = p * (xp - x[j])/(x[i] - x[j])

  yp = yp + p * y[i]

#Displaying output
print ()
print('Nilai interpolasi untuk %.3f adalah %.3f.' % (xp, yp))
