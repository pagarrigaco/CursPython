from random import shuffle

#JOC DE LA PALLETA MÉS CURTA
#llista inicial
palletes =['-','--','---','----']

#barrejar palletes
def barrejar(llista):
    shuffle(llista)
    return llista

#demanar a l'usuari que agafi palleta
def torn_jugador():
    intent =''

    while intent not in ['1','2','3','4']:
        intent = input("Escull un número del 1 al 4: ")

    return int(intent)

#comprovar l'intent
def comprovar_resultat(llista,intent):

    print(f"Has escollit la palleta {llista[intent-1]}")
    if llista[intent-1] == '-':
        print("Has agafat la palleta més curta!")
    else:
        print("Has tingut sort!")

#MAIN
palletesbarrejades = barrejar(palletes)
opcio = torn_jugador()
comprovar_resultat(palletesbarrejades,opcio)