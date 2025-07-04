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
print(myTupla) #mutable

#recorrer una array y hacer una operación de forma imperativa o declarativa
for i in myArray:
      print(i)



import time

# Lista de ejemplo grande para notar la diferencia
myArray = list(range(1, 10000000))

# Imperativo: usando for
#Le dices a la computadora exactamente cómo hacerlo, paso a paso
start = time.time()
result_for = []
for x in myArray:
    result_for.append(x * 2)
end = time.time()
print(f"Tiempo con for: {end - start:.6f} segundos")

# Declarativo: usando list comprehension
# Le dices a la computadora qué resultado quieres.
# Forma pythonica
# Los corchetes indican que el resultado será una lista.
start = time.time()
result_comp = [x * 2 for x in myArray]
end = time.time()
print(f"Tiempo con list comprehension: {end - start:.6f} segundos")

# Declarativo: usando map
start = time.time()
result_map = list(map(lambda x: x * 2, myArray))
end = time.time()
print(f"Tiempo con map: {end - start:.6f} segundos")


import this





