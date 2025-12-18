alien_0 = {'color':'verd','punts':5}
print(alien_0['color'])
print(f"Has guanyat {alien_0['punts']} punts")

alien_0['pos_x']=0
alien_0['pos_y']=25

print(alien_0['pos_x'])

llenguatge_preferit ={
    'pau' : 'Python',
    'montse' : 'C#',
    'júlia' : 'Java',
    'àlex' : 'Pico8'
}

llenguatge_01 = llenguatge_preferit.get('Mark','Aquesta variable no està definida')
llenguatge_02 = llenguatge_preferit.get('montse','Aquesta variable no està definida')

print(llenguatge_01)
print(llenguatge_02)

for nom,valor in llenguatge_preferit.items():
    print(f"En/La {nom.title()} prefereix programar en {valor}")

for nom in llenguatge_preferit.keys():
    print(f"Hola {nom.title()}")
for valor in llenguatge_preferit.values():
    print(f"Llenguatge {valor}")

pizza ={
    'massa':'fina',
    'tamany':'familiar',
    'ingredients':['ceba','bacon','carn','sala barbacoa','xampinyons']
}
print(f"Tipus de massa: {pizza['massa']}")
print(f"Tamany: {pizza['tamany']}")
i = 1
for complement in pizza['ingredients']:
    print(f"\tIngredient {i}: {complement}")
    i=i+1
