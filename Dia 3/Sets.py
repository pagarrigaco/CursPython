set = set([1,2,3,4])
set2 = {4,5,6,7,8,9}

set3 = set.union(set2)

set.add(5) #afegeix
set.remove(2) #elimina. Si no existeix produeix un error
set.discard(9) #no dona error si no existeix

set.pop() #en aquest cas elimina aleatoriament un element

set.clear() #neteja el set

print(set)
print(len(set))
print(2 in set)
print(set3) #elimina els repetits
