# Her n 1,2,3... icin n'nin bir asal sayi ya da asal sayiların carpimi oldugunu gosteren kod.
# Tabii ki sonsuza giden degerleri gostermiyor teknolojinin izin verdigi kadarini gorebiliyoruz.

print("Bir n sayisi girin:")
n = int(input())
m = n
array = [2, 3]
array1 = []

for i in range(2, n + 1):
    for j in range(2, i - 1):
        if i % j == 0:
            break
        elif j == i - 2:
            array.append(i)

for i in range(len(array)):
    a = array[i]
    if n % a == 0:
        while n % a == 0:
            array1.append(a)
            n /= a

print('n')
print(array1)
print("sayilarinin carpimina esittir.")
