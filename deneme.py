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

"""
squares = [i * i for i in range(1, 14)]


print(squares)
"""

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
"""
i = 3
d = 2.8
s = 'is my favorite platform!'

    16

    8.0

    HackerRank is the best place to learn and practice coding!

    
    7

    6.8

    HackerRank is my favorite platform!
"""   
    
a = 12
b = 4.0
c = "is the best place to learn and practice coding!"

q = 4
w = 4.0
e = "HackerRank "
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line


if i == 4:
    print(i + a)
    print(d + b)
    print(s + c)    
else:
    print(i + q)
    print(d + w)
    print(s + e) 
    
# The 's' variable above should be printed first.

