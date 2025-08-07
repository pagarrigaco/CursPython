comparacio = (4<5) and (5==24) #les dues s'han de complir
comparacio2 = (4<5) or (5==24) #només cal que una sigui veritat

text = "aquesta frase es breu"

cerca = ("frase" in text) and ("breu" in text)
negativa = not 1 == 1
print(comparacio)
print(comparacio2)
print(cerca)
print(negativa)