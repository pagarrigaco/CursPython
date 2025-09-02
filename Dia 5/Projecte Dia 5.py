from random import choice

paraules = ["HOLA","PAPALLONA","VEHICLE","COTXE","CASA", "GOS", "GAT", "TAULA", "CADIRA", "LLIBRE", "ORDINADOR", "CIUTAT",
    "CARRER", "ARBRE", "PLATJA", "MUNTANYA", "AIGUA", "FOC", "VENT", "TERRA", "CEL", "SOL", "LLUNA", "ESTRELLA", "FLOR", "FRUITA",
    "PORTA" "FINESTRA", "MURMURI", "BICICLETA", "TREN", "PAPER", "VAIXELL",
    "AMISTAT", "ROSSEGADOR", "AMOR", "IOGURT", "SOMNI", "PARAULA", "TEMPS",
    "ESCOLA", "LLANTERNA", "TREBALL", "JOC", "RIURE", "CONILL", "OMBRA",
    "ESTANTERIA", "ULL", "MOSQUIT", "COR", "NATURA"]
abc = [chr(ord('A') + i) for i in range(26)]
lletra =''
vides = 11
utilitzades =['']

def escollir_paraula(llista): #ESCULL UNA PARAULA PER ENDEVINAR
    paraula = choice(llista)
    return paraula

def mostrar_guions(paraula): #MOSTRAR ELS GUIONS I CREAR LLISTA AMB LES LLETRES DE LA PARAULA
    longitud = len(paraula)
    guions = []
    nova_paraula = []
    for n in range(longitud):
        guions.append('-')
    for x in paraula:
        nova_paraula.append(x)
    return nova_paraula,guions

def nova_lletra(utilitzades):
    lletra =''
    while not(lletra in abc and lletra not in utilitzades):
        lletra = input("Quina lletra vols provar? ")
        lletra = lletra.upper()
        if lletra not in abc:
            print("No és un caràcter vàlid")
        elif lletra in utilitzades:
            print("Ja has fet servir aquesta lletra")
    utilitzades.append(lletra)
    return lletra, utilitzades

def existeix_lletra(paraula, lletra):
    return paraula.find(lletra.upper())

def mostrar_lletra(paraula,lletra,guions):
    posicio_lletra = []
    for i in range(len(paraula)):
        if paraula[i] == lletra:
            posicio_lletra.append(i)
    for x in range(len(posicio_lletra)):
        pos = posicio_lletra[x]
        guions[pos] = lletra
    return (guions)

def resultat(trobada,paraula):
    if trobada:
        print()
        print(f"FELICITATS! HAS ACONSEGUIT DESCOBRIR LA PARAULA {paraula}")
    else:
        print()
        print("HO SENTO, MÉS SORT LA PROPERA VEGADA!")
        print(f"La paraula que buscaves era {paraula}")

def jugada (vides,trobada,guions,utilitzades,paraula,llista_lletres):
    while vides > 0 and not (trobada):
        print(f"La paraula a endevinar és: {guions}")
        print(f"Tens {vides} intents")
        print()
        lletra, utilitzades = nova_lletra(utilitzades)
        if (existeix_lletra(paraula, lletra)) != -1:
            print(f"La lletra {lletra} existeix dins la paraula")
            guions = mostrar_lletra(llista_lletres, lletra, guions)
            if '-' not in guions:
                trobada = True
        else:
            print(f"La lletra {lletra} no existeix dins la paraula")
            vides = vides - 1
    return trobada

#MAIN
print()
print ("BENVINGUT AL JOC DEL PENJAT!")
print()
paraula = escollir_paraula(paraules)
llista_lletres, guions = mostrar_guions(paraula)
trobada = False
trobada = jugada(vides,trobada,guions,utilitzades,paraula,llista_lletres)
resultat(trobada,paraula)