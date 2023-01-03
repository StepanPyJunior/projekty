import random

class Postavy:
    def __init__(self, jmeno, cech):
        self.jmeno = jmeno
        self.cech = cech

    def informace(self):
        print("\nJméno postavy:", self.jmeno, "\nČlenem cechu:", self.cech + "ů")

seznam_cechu = {1: "Válečník", 2: "Kouzelník", 3: "Zloděj"}

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

hlavni_hrdina = Postavy(jmeno_hrace, cech_hrace)




