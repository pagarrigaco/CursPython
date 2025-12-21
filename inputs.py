nom = input("Introdueix el teu nom: ")
print(nom)

prompt = ("Has entrat al nostre sistema")
prompt += ("\nIntrodueix el teu nom d'usuari: ")

user = input (prompt)
print((f"Benvingut, {user}"))

edat = input("Introdueix la teva edat: ")
edat = int(edat)

if edat>=18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")