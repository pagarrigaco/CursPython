def suma(**kwargs):
    suma_total=0
    for clau,valor in kwargs.items():
        print(f"La clau és {clau} i el valor {valor}")
        suma_total += valor
    return suma_total


suma_final =suma(x=3,y=5,Z=2)

print(f"La suma total és: {suma_final}")

def describir_persona(nom,**kwargs):
    print(f"Características de {nom}:")
    for clau, valor in kwargs.items():
        print(f"{clau}:{valor}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")