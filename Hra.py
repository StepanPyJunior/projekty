import random

class Postavy:
    def __init__(self, jmeno, cech, mince=0):
        self.jmeno = jmeno
        self.cech = cech
        self.mince = mince

    def informace(self):
        print("\nJméno postavy:", self.jmeno, "\nČlenem cechu:", self.cech + "ů \nPočet mincí:", self.mince)

seznam_volba = [1, 2, 3]
seznam_cechu = {1: "Válečník", 2: "Kouzelník", 3: "Zloděj"}
seznam_zbrani = {1: "větev", 2: "dvouruční sekera", 3: "kouzelnická hůl", 4: "dýka"}
mince_hrace = 0
vypita_piva = 0
osloveni = ""

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
    osloveni = "válečník"
elif cech_hrace == seznam_cechu[2]:
    osloveni = "čaroděj"
else:
    osloveni = "zloděj"

if cech_hrace == seznam_cechu[1]:
    zakladna = "aréně"
elif cech_hrace == seznam_cechu[2]:
    zakladna = "akademii"
else:
    zakladna = "krčmě"

print("Vítej v", zakladna, jmeno_hrace,"\n")

print("V", zakladna,"se prochází jeden tajemný pocestný a u stolu naproti tobě sedí postarší",osloveni,)

while True:
    volba = input(f"1. Promluvit s pocestným.\n2. Promluvit s postarším {osloveni}em.\n3. Dát si pivo.\n")
    if volba.isdigit():
        volba = int(volba)
        if volba not in seznam_volba:
            print("Zadej číslo od 1 do 3.")
            continue
        else:
            if volba == 1:
                print("Pocestný se na tebe divně podivá, něco zamumlá a otočí se k tobě zády.\n")
                continue
            elif volba == 3:
                print("Hodíš do sebe jedno pivo a hned se cítíš o něco líp.\n")
                vypita_piva += 1
                continue
            else:
                while True:
                    volba = input("\n" + osloveni.capitalize() + " se na tebe podívá a začne ti vyprávět o tlupě zlodějů co terorizuje okolí"
                                                             "a že by jim někdo měl konečně dát lekci\n1. Zeptat se více na lapky."
                                                             "\n2. Zeptat se na odměnu za dopadení lapků.\n3. Dát si pivo.\n")
                    if volba.isdigit():
                        volba = int(volba)
                        if volba not in seznam_volba:
                            print("Zadej číslo od 1 do 3.")
                            continue
                        else:
                            if volba == 1:
                                print("\n" + osloveni.capitalize() + " ti začně vyprávět o tom jak lapkové okrádají místní farmáře a že jsou farmáři"
                                                                      "ochotni zaplatit za jejich dopadení.\n")
                                break
                            elif volba == 3:
                                vypita_piva += 1
                                print(f"\nDal sis " + str(vypita_piva) + ". pivo a začínají se ti podlamovat kolena.\n")
                                break
                            else:
                                print("\nOdměna za dopadení lapků je 100 měďáků.\n")
                                break
                    else:
                        print("Zadej platnou volbu.")
                        continue
            break
    else:
        print("Zadej platnou volbu.")
    continue