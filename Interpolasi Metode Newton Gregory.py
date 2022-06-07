import numpy as np

n = int(input("Masukkan jumlah pasang nilai: "))
x = np.zeros(n)
y = np.zeros(n)
SM = np.zeros((n,n))

for k in range(0,n):
    print('Masukkan x[{}] = '.format(k), end = ' ')
    x[k] = float(input())
    print('Masukkan y[{}] = '.format(k), end = ' ')
    y[k] = float(input())
    SM[k,0] = y[k]

X = float(input("Masukkan nilai x yang ingin dicari pasangannya: "))

def faktorial(i):
    fak = 1
    for k in range(2,i+1,1):
        fak *= k
    return fak

for k in range(1,n):
    for i in range(0,n-k):
        SM[i,k] = SM[i+1,k-1] - SM[i,k-1]

h = x[1] - x[0]
p = (X - x[0])/h

Y = SM[0,0]
for i in range(1,n):
    suku = SM[0,i]
    for k in range(0,i):
        suku *= (p - k)
    suku = suku/faktorial(i)
    Y = Y + suku

print("Hasilnya adalah: ", Y)