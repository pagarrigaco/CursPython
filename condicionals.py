complements = ['bolets','ceba','bacon','formatge']
sopar = "pizza"
numero = 3
nota = 12

if sopar =="pizza":
    print("Hi ha pizza per sopar")

if 'ceba' in complements:
    print("I porta ceba!")
if numero <= 5:
    print("Surt a cinc talls per cap!")

for ingredient in complements:
    if ingredient == 'bacon':
        print(f"Ens hem quedat sense {ingredient}")
    else:
        print(f"Afegint {ingredient} a la pizza")

if nota <5:
    print("Has suspès!")
elif nota <6:
    print("Has aprovat amb un suficient")
elif nota <7:
    print("Has aprovat amb un bé")
elif nota <8:
    print("Has aprovat amb un notable")
elif nota <10:
    print("Has aprovat amb un excel·lent")
else:
    print("No t'has presentat a l'examen")