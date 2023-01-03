import random

print("Vítej ve hře kámen nůžky papír.")

hrac_vyhry = 0
pocitac_vyhry = 0
volby = ["kámen", "nůžky", "papír"]

while True:
    hrac_volba = input("\nPro hru zvol jednu ze tří možností: kámen/nůžky/papír. Pro konec hry zvol Q.\n").lower()
    if hrac_volba == "q":
        break
    if hrac_volba not in volby:
        print("\nZadej platnou možnost kámen/nůžky/papír.")
        continue

    nahodne_cislo = random.randint(0,2)
    pocitac_volba = volby[nahodne_cislo]

    if hrac_volba == "kámen" and pocitac_volba == "nůžky":
        hrac_vyhry += 1
        print("Vyhrál jsi!")
    elif hrac_volba == "nůžky" and pocitac_volba == "papír":
        hrac_vyhry += 1
        print("Vyhrál jsi!")
    elif hrac_volba == "papír" and pocitac_volba == "kámen":
        hrac_vyhry += 1
        print("Vyhrál jsi!")
    elif hrac_volba == pocitac_volba:
        print("Remíza!")
    else:
        pocitac_vyhry += 1
        print("Vyhrál počítač!")

if hrac_vyhry > pocitac_vyhry:
    vitez = "Vyhrál jsi ty"
elif hrac_vyhry < pocitac_vyhry:
    vitez = "Vyhrál počítač"
else:
    vitez = "Remíza."

print("\nZískal jsi", hrac_vyhry, "vítězství.")
print("Počítač získal", pocitac_vyhry, "vítězství.")
print("Výsledek je:", vitez)
print("\nKonec hry")