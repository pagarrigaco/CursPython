diccionari = {'c1':'valor1','c2':'valor2','c3':'valor3'}
client = {'Nom':'Pau','Cognom':'Garriga','pes':89,'alcada':1.80}
dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}} #pot tenir qualsevol tipus de valor
exercici = {'c1':['a','b','c'], 'c2':['d','e','f']}
dic1 ={1:'a',2:'b'}

print(dic1)

dic1[3] ='c' #afegir contingut al diccionari

print(dic1)

dic1[1] ='Z'

print(dic1)
print(dic1.keys())
print(dic1.values())
print(dic1.items())

consulta = (client['Cognom'])

print(consulta)
print(dic['c2'][1])
print(dic['c3']['s2'])
print(exercici['c2'][1].upper())


