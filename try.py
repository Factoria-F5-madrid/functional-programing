x = 2
y = 3

print(x + y)

# if = 3 # error léxico/sintáctico

z = 2
w = '3'

#print(z + w) error de tipado

myArray = [1, 2, 3, 4, 5]
myArray.append(6)
myArray[0] = 2
print(myArray) #mutable

myTupla = (1, 2, 3, 4, 5)
#myTupla.append(6)
#myTupla[0] = 2 no support
print(myTupla) #nomutable

#recorrer una array y hacer una operación de forma imperativa o declarativa
for i in myArray:
      print(i)

from statistics import median
from timeit import repeat

def duplicar_for(numeros):
    resultado = []
    for numero in numeros:
        resultado.append(numero * 2)
    return resultado

def duplicar_comprehension(numeros):
    return [numero * 2 for numero in numeros]

def duplicar_map(numeros):
    return list(map(lambda numero: numero * 2, numeros))

numeros = list(range(1, 100001))

for nombre, funcion in [
    ("for", duplicar_for),
    ("list comprehension", duplicar_comprehension),
    ("map", duplicar_map),
]:
    tiempos = repeat(lambda: funcion(numeros), repeat=7, number=1)
    print(f"Tiempo mediano con {nombre}: {median(tiempos):.6f} segundos")


# import this





