tupla = (1,2,3,4,1,3,4,5,6,7)
tupla2 = (1,2,(10,20,30),4,5)
t =(1,2,3)

x,y,z = t

print(type(tupla))
print(tupla)
print(tupla[0])

print(x,y,z)
print(x)
print(tupla.count(1)) #conta les vegades que surt un valor
print(t.index(2)) #primera posició on apareix un valor

print(tupla2[2][1])