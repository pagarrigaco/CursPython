import pizza
#si només volem importar una funció concreta d'un mòdul FROM PIZZA IMPORT CUINAR_PIZZA
#podem posar un alias IMPORT PIZZA AS P
#podem posar un alias a la funció FROM PIZZA IMPORT CUINAR_PIZZA AS CP

def saluda():
    print("Hola")

def saluda2 (nom,carrec):
    print(f"Bon dia {nom.title()}, ets el nou {carrec}")

def suma(valor1,valor2):
    total = valor1+valor2
    return total

def saluda3 (noms):
    for nom in noms:
        print(f"Benvingut/da {nom}")
'''
def fer_pizza(*ingredients):
    print("Per fer una pizza necessitem:")
    for items in ingredients:
        print(f"\t- {items}")
'''
treballadors =['Pau','Montse','Júlia','Àlex']

saluda3(treballadors)
print('\n')
saluda()
print('\n')
saluda2('Pau','Director')
print('\n')
resultat = suma(20,5)
print(resultat)
print('\n')
pizza.fer_pizza('ceba')
print('\n')
pizza.fer_pizza('ceba','bacon','xampinyons')
