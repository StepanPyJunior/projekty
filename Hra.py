import random

class Postavy:
    def __init__(self, jmeno, cech, mince=0):
        self.jmeno = jmeno
        self.cech = cech
        self.mince = mince

    def informace(self):
        print("\nJméno postavy:", self.jmeno, "\nČlenem cechu:", self.cech + "ů \nPočet mincí:", self.mince)

seznam_cechu = {1: "Válečník", 2: "Kouzelník", 3: "Zloděj"}
seznam_zbrani = {1: "větev", 2: "dvouruční sekera", 3: "kouzelnická hůl", 4: "dýka"}
mince_hrace = 0

jmeno_hrace = input("Vítej ve hře na hrdiny. Jak se jmenuješ?\n")
print("\nVýborně, od teď budeš znám jako", jmeno_hrace)

while True:
    cech_hrace = input("\nNyní si vyber cech\n1. Cech válečníků\n2. Cech kouzelníků\n3. Cech zlodějů\n")
    if cech_hrace.isdigit():
        cech_hrace = int(cech_hrace)
        if cech_hrace not in seznam_cechu:
            print("Zadej číslo od 1 do 3.")
            continue
        else:
            cech_hrace = seznam_cechu[cech_hrace]
            print("\nPřidal jsi se k cechu", cech_hrace + "ů.")
            break
    else:
        print("Zadej číselnou hodnotu!")
        continue

hlavni_hrdina = Postavy(jmeno_hrace, cech_hrace, mince_hrace)

if cech_hrace == seznam_cechu[1]:
    osloveni = "válečníku"
elif cech_hrace == seznam_cechu[2]:
    osloveni = "čaroději"
else:
    osloveni = "zloději"

if cech_hrace == seznam_cechu[1]:
    zakladna = "aréně"
elif cech_hrace == seznam_cechu[2]:
    zakladna = "akademii"
else:
    zakladna = "krčmě"

print("Vítej v", zakladna, osloveni)


