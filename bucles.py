i = 1

while i<=5:
    print(i)
    i+=1

prompt= ("Repetiré el que tu escriguis fins")
prompt +=("\nque diguis prou: ")


text=""
while text != "prou":
    text=input(prompt)
    if text != "prou":
        print(text)

animals = ['gat','gos','cavall','gat','serp','gat','os']
print(animals)

while 'gat' in animals:
    animals.remove('gat')
print(animals)
