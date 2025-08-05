from ftplib import print_line

text = input("Introdueix el text que vols analitzar: ")
lletres = []
lletres.append(input("Introdueix la primera lletra: ").lower())
lletres.append(input("Introdueix la segona lletra: ").lower())
lletres.append(input("Introdueix la tercera lletra: ").lower())
ll = input("Introdueix la primera lletra: ").lower()
lletra1 = text.count(ll)
lletra2 = text.count(lletres[1])
lletra3 = text.count(lletres[2])

print("\n")
print(f"Hem trobat un total de {lletra1} lletres '{ll}' ")
text_aux = text
text_aux = text_aux.lower()
existeix = ("python" in text)
trobat = "He trobat la paraula Python en aquest text"
no_trobat = "No he trobat la paraula Python en aquest text"
dic = {False:no_trobat, True:trobat}

llista = text.split(" ")
print_line(f"\nAquest text té un total de {len(llista)} paraules") #comptem les paraules que formen el text
print_line(f"\nLa primera lletra d'aquest text és la {text[0]} i la última és la {text[-1]}") #presentem la primera i l'última lletra
llista.reverse()
inversa = " ".join(llista)
print_line(f"Així és com quedaria aquest text a l'inversa: {inversa}")
print_line(dic[existeix])

