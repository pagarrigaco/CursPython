nom = input("Digues el teu nom: ")
vendes = input("Quantes vendes has fet? ")

vendes = int(vendes)

comissio = vendes * 13 /100

print(f"Bon dia {nom} la teva comissió d'aquest mes és de: {round(comissio,2)} euros")