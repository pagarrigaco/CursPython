preus_cafe = [('Cafè sol', 2.4),('Tallat',1.2),('Cafè amb llet', 1.9)]
'''
for cafe, preu in preus_cafe:
    print(cafe)
'''

def cafe_mes_car(llista_preus):
    preu_maxim = 0
    tipus =''

    for cafe,preu in llista_preus:
        if preu > preu_maxim:
            preu_maxim = preu
            tipus = cafe
        else:
            pass
    return (preu_maxim, tipus)

preu,cafe = cafe_mes_car(preus_cafe)
print(f"El cafè més car és el tipus {cafe} amb un preu de {preu} euros")

