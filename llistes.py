noms=['pau','montse','júlia','àlex']

print(noms[1])
print(f"El meu nom és {noms[0].title()}")

for name in noms:
    print(name.title())
# 0 a 5
for value in range(6):
   print(value)
# 1 a 4
for valor in range(1,5):
    print(valor)

numeros =list(range(1,6))

print(numeros)

#exemple
quadrats=[]
for nums in range(1,11):
    valor = nums**2
    quadrats.append(valor)
print(quadrats)