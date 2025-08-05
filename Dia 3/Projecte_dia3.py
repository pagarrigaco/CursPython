text = input("Introdueix el text que vols analitzar: ")
text_aux = text.lower()

lletra1 = input("Introdueix la primera lletra: ").lower()
lletra2 = input("Introdueix la segona lletra: ").lower()
lletra3 = input("Introdueix la tercera lletra: ").lower()

num_lletra1 = text.count(lletra1)
num_lletra2 = text.count(lletra2)
num_lletra3 = text.count(lletra3)
diccionari = {True:"He trobat la paraula Python en aquest text", False:"No he trobat la paraula Python en aquest text"}

llista = text.split(" ")

print("\n")
#comptem les vegades que apareixen les lletres que ha introduit l'usuari
print(f"Hem trobat un total de {num_lletra1} lletres '{lletra1}', {num_lletra2} lletres '{lletra2}' i {num_lletra3} lletres '{lletra3} en aquest text")
#comptem el número de paraules del text
print(f"Aquest text té un total de {len(llista)} paraules")
#Indiquem quina és la primera lletra i quina és la última
print(f"La primera lletra d'aquest text és la lletra '{text[0]}' i la última és la lletra '{text[-1]}'")
#mostrem el text a l'inversa
llista.reverse()
inversa = " ".join(llista)
print(f"Així quedaria aquest text a l'inversa: '{inversa}'")
#mirem si existeix la paraula Python dins el text
existeix = ("Python" in text)
print(diccionari[existeix])

