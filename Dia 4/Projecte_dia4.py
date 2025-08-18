from random import *

jugar = True

nom = input("Introdueix el teu nom: ")
print(f"Benvingut {nom}, he pensat un número entre 1 i 100, tens 8 intents per endevinar-lo. Prepara't per jugar?")

while (jugar):

    aleatori = randint(1,100)
    no_trobat = True
    i = 1

    while (no_trobat) and (i<8):
        print(f"Intent número {i}")
        num = input("Introdueix el número: ")
        if (int(num) < 1) or (int(num) > 100):
            print("Has introduit un número incorrecte")
        elif int(num) > aleatori:
            print("El número que has escollit és més gran")
        elif int(num) < aleatori:
            print("El número que has escollit és més petit")
        elif int(num) == aleatori:
            no_trobat = False
        i +=1

    if (no_trobat == False):
        print(f"Felicitats! Has tardat {i-1} intents per encertar el número {aleatori}")
    else:
        print("Llàstima, no has endevinat el número")


    opcio = input("Vols fer una altra partida? (s/n)")
    if opcio == 's':
        jugar = True
    elif opcio == 'n':
        jugar = False







