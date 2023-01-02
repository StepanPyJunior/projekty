import random

while True:
    a = input("Zadej cislo: ")
    if a.isdigit():
        break
    else:
        print("Zadej pouze cislo!")
        continue

a = int(a)
print("Zadal jsi cislo", a,". Hledej cislo od 0 do", a,)
r = random.randint(0, a)

c = 0
d = ""

while True:
    b = input("Zadej svuj tip hledaneho cisla ")
    if b.isdigit():
        print("Zadal jsi cislo", b,)
    else:
        print("Zadej cislo!")
        continue
    b = int(b)
    c += 1
    if b == r:
        print("Tvuj tip je spravny, gratuluji!")
        break
    elif b > r:
        print("Tvuj tip je vetsi nez hledane cislo")
        continue
    else:
        print("Tvuj tip je mensi nez hledane cislo")
        continue

if c > 4:
    d = "pokusu"
else:
    d = "pokusy"

print("Tipnout spravne cislo ti zabralo", c, d,"gratuluji!")