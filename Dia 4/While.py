monedes = 5
resposta = 's'

while monedes > 0:
    print(f"Tens {monedes} monedes")
    monedes -=1
else:
    print("No et queden monedes")

while resposta == 's':
    resposta = input ("Vols seguir? (s/n) ")
else:
    print("Gràcies per utilitzar el programa")

nom = "Montserrat"

for lletra in nom:
    if lletra == 'r':
        break
    print(lletra)
