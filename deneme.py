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
