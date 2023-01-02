print("Vítej v programu Kvíz")

c = 0
a = input("Kolik je 2 + 2? ")
if a == "4":
    print("Správná odpověď")
    c += 1
else:
    print("Špatná odpověď")

b = input ("Kolik je 2 x 3? ")
if b == str(2 * 3):
    print("Správná odpověď")
    c += 1
else:
    print("Špatná odpověď")

d = input ("Kolik je 3 x 3? ")
if d == str(3 * 3):
    print("Správná odpověď")
    c += 1
else:
    print("Špatná odpověď")

print("Odpověděl jsi správně na " + str(c) + " otázky a tvá úspěšnost je " + str(round(float(c)/3*100, 1)) + "%")