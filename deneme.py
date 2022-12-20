""" bankamatik
x = int(input("para çekmek için 1'e basın:"))

if x == 1:
    y = int(input("miktarı girin:"))
    if y >= 1000:
        print("güle güle harca")
    else:
        print("sg fakir")

else:
    print("görüşürüz")
"""

"""
cevap = input("x\'in değeri 2 olsun mu? y/n:")

if cevap == "y":
    x = 2
else:
    x = 0

print(x)
"""

"""
cevap = input("x\'in değeri 2 olsun mu? y/n:")

x = 2 if cevap=="y" else 0

print(x)
"""

"""
x = int(input("çift bir sayı giriniz:"))

while x % 2 != 0:
    print("çift sayı girsene gardaş!?!?!")
    x = int(input("çift bir sayı giriniz:"))
print("aferin")
"""

"""
x = 0 

while x < 15:
    print(x)
    x = x + 1

print("yeter")
"""

"""
toplam = 0
x = 0

while x < 59:
    toplam = x + 5
    x = x + 7
print(toplam)
"""

"""
l = ["d", "fd", "k", "ba"]
print(sorted(l))
"""

"""
x = 10
y = 20

konum = (x, y)

print(konum)
"""

"""
maas = [10000, 15000, 20000]
kisi = ["ahmet", "mehmet", "ayşe"]
"""

"""
genelmaas = {"ahmet": 10000, "mehmet": 15000, "ayşe": 20000}
genelmaas["fatma"] = 30000
print(genelmaas)
print("hasan" in genelmaas)
print("ayşe" in genelmaas)
"""
"""
if __name__ == '__main__':
    n = int(input())

x = -1
while 0 < n:
    x = x + 1
    n = n - 1
    y = x * x
    print(y)
"""

"""
notlar = [4, 5, 6, 7, 8, 34, 54, 65]
t = 0
for e in notlar:
    t += e

ortalama = t / len(notlar)

print(ortalama)

for o in range(len(notlar)):
    print(notlar[o])
    break

for o in range(len(notlar)):
    t += notlar[o]
ortalama = t / len(notlar)
print("ortalama", ortalama)
"""

"""
s = "merhaba nasılsın ?"

print(s.split(" "))


l = ['asda', 'fgdf', 'rtyrty']
print(".".join(l))
"""


squares = []


print(squares=[i * i for i in range(1, 11)])
