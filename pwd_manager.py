master_pwd = input("Zadejte master password: ")

if master_pwd != "Heslo123":
    print("Nesprávné heslo.")
    print("Konec programu.")
    quit()

def pridat():
        while True:
            jmeno = input("Zadejte uzivatelske jmeno: ")
            heslo = input("Zadejte heslo: ")
            sifrovane_jmeno = ""
            sifrovane_heslo = ""

            for znak in jmeno:
                sifrovane_jmeno += chr(ord(znak) + 5)

            for znak in heslo:
                sifrovane_heslo += chr(ord(znak) + 5)

            if " " in jmeno or " " in heslo:
                print("Jméno ani heslo nesmí obsahovat mezeru.")
                continue
            else:
                with open("pwd_manager.txt", "a") as soubor:
                    soubor.write(sifrovane_jmeno + " " + sifrovane_heslo + "\n")
                    break
        return sifrovane_jmeno, sifrovane_heslo

def zobrazit():
    with open("pwd_manager.txt", "r") as soubor:
        puvodni_jmeno = ""
        puvodni_heslo = ""

        for znak in sifrovane_jmeno:
            puvodni_jmeno += chr(ord(znak)-5)

        for znak in sifrovane_heslo:
            puvodni_heslo += chr(ord(znak)-5)

        for line in soubor.readlines():
            hesla = line.rstrip()
            jmeno, heslo = hesla.split(" ")
            print("Login:", puvodni_jmeno, "\nPassword:", puvodni_heslo, "\n")

while True:
    vstup = input("Jakou funkci chcete provést?\n1. Přidat nové.\n2. Zobrazit vše.\nQ - zavřít program.\n").lower()
    if vstup == "q":
        break

    if vstup == "1":
        pridat()
    elif vstup == "2":
        zobrazit()
    else:
        print("Zadejte platnou volbu.")
        continue

print("Konec programu.")