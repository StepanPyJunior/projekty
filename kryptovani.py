text = input("Zadej zprávu pro kryptování")

x = ""

for znak in text:
    x += chr(ord(znak)+2)

print(x)

puvodni = ""

for znak in x:
    puvodni += chr(ord(znak)-2)

print(puvodni)