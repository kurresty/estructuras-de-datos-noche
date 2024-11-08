# ejemplo con tuplas
tupla1 = {}#tupla vacia
print(tupla1)

tupla2 = ("apple",2018,"samsung",4.9,"t",True)
print(tupla2)
print(tupla2[1])
print(tupla2[3])

#operacion con tuplas
tupla3 = ("A","B","C","D")
tupla4 =(1,2,3,4)

#concatenar
tupla5 = tupla3 + tupla4
print(tupla5)

#repetir
tupla6 = tupla3 * 3
print(tupla6)

# tupla enlazada
tupla7 = (0,1,2,3)
tupla8 = ("A","B","C")
tupla9 = (tupla7,tupla8)
print(tupla9)
print(tupla9[1])
print(tupla9[1][1])
print(tupla9[1][2])

#comparar
tupla10 = ("Rojas")
ttupla11 = (123)
tuploa12 = ("Rosas")
tupla13 = ("rosas")
print(tupla10 < tuploa12)
