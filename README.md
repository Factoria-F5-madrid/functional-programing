# Programación Funcional

## Índice

1. [Introducción](#1-introducción)
2. [Conceptos Fundamentales](#2-conceptos-fundamentales)
3. [Principios Básicos de la Programación Funcional](#3-principios-básicos-de-la-programación-funcional)
4. [Funciones Puras](#4-funciones-puras)
5. [Inmutabilidad](#5-inmutabilidad)
6. [Composición de Funciones](#6-composición-de-funciones)
7. [Uso de Funciones de Orden Superior](#7-uso-de-funciones-de-orden-superior)
8. [Ejemplo Completo en Python](#8-ejemplo-completo-en-python)
9. [Ventajas y Desventajas de la Programación Funcional](#9-ventajas-y-desventajas-de-la-programación-funcional)
10. [Recursos Adicionales](#10-recursos-adicionales)

---

## 1. Introducción

La programación funcional es un paradigma de programación que trata de construir programas mediante el uso de funciones puras, evitando el estado compartido, los efectos secundarios y los datos mutables. Es una forma declarativa de programar que se enfoca en el **"qué"** en lugar del **"cómo"**.

🚀 **Características clave**:
- Uso extensivo de funciones.
- Inmutabilidad como base.
- Composición y reutilización de funciones.

📖 **Historia**: Inspirada en el cálculo lambda desarrollado por Alonzo Church (director de Alan Turing) en la década de 1930, la programación funcional ha influido en lenguajes modernos como Haskell, Lisp, Scala, JavaScript, Python, y otros.

```
El nombre de las funciones no importa, solo importa lo que hacen
Esto: suma(x, y) = x + y es igual a esto: (x, y) = x + y

En el cálculo lambda, los nombres de las variables son simbólicos y no afectan el significado de la función. Lo importante es cómo se utilizan.

Esto: (x, y) = x + y es igual a esto: (a, b) = a + b
```

---

## 2. Conceptos Fundamentales

📌 **Función**: Una función es una relación entre una entrada y una salida donde cada entrada tiene exactamente una salida.

![Batidora](https://jorgebenitezlopez.com/tiddlywiki/pro/batidora.png)

📌 **Función pura**: No tiene efectos secundarios y siempre produce el mismo resultado para las mismas entradas.

📌 **Efectos secundarios**: Cambios en el estado externo o cualquier acción que ocurra fuera de la función, como modificar variables globales, escribir en un archivo o mostrar algo en pantalla.

📌 **Inmutabilidad**: Los datos no cambian. En lugar de modificar una estructura de datos, se crea una nueva. 

> [!WARNING]
> Por ejemplo, cuando analicemos y limpiemos datos, es importante trabajar sobre una copia de los datos, no sobre el archivo original

---

## 3. Principios Básicos de la Programación Funcional

1. **Funciones puras**: El comportamiento de la función depende solo de sus entradas.
2. **Inmutabilidad**: Los datos no cambian después de ser creados.
3. **Funciones de orden superior**: Las funciones pueden ser pasadas como argumentos y devueltas como valores.
4. **Composición de funciones**: Combinar funciones simples para crear funciones más complejas.
5. **Evitar efectos secundarios**: No modificar el estado global ni interactuar directamente con el entorno.

---

## 4. Funciones Puras

Una función pura es determinista y no tiene efectos secundarios.

**Ejemplo en Python:**
```python
def suma(a, b):
    return a + b

print(suma(2, 3))  # Siempre devuelve 5
print(suma(2, 3))  # Siempre devuelve 5, sin importar cuántas veces se llame
```

🚨 ¿Cómo sería una función impura? 🚨

```python
resultado_global = 0  # Estado externo

def suma_impura(a, b):
    global resultado_global  # Modifica una variable externa (efecto secundario)
    resultado_global += a + b
    return resultado_global

# Llamadas a la función
print(suma_impura(2, 3))  # Output: 5
print(suma_impura(2, 3))  # Output: 10 (resultado cambia porque modifica el estado global)
```

## 5. Inmutabilidad

En programación funcional, los datos no se modifican; en su lugar, se crean nuevos datos.

**Ejemplo en Python (usando `map`):**
```python
arr = [1, 2, 3]
doubled = list(map(lambda x: x * 2, arr))

print(doubled)  # [2, 4, 6]
print(arr)      # [1, 2, 3] (sin cambios)
```

> [!WARNING]
> map toma una función y una colección (lista, tupla, etc.) por lo que es una función de orden superior y devuelve un nuevo iterable, lo que es una característica clave de la programación funcional (Inmutabilidad)

🚨 ¿Cómo sería algo mutable? 🚨

```python
arr = [1, 2, 3]
for i in range(len(arr)):
    arr[i] *= 2  # Modifica directamente los valores de la lista

print("Modified:", arr)  # [2, 4, 6]
```

## 6. Composición de Funciones

La composición de funciones consiste en combinar múltiples funciones simples para formar una nueva función más compleja. Esto es útil para mantener el código modular y reutilizable.

**Ejemplo en Python:**
```python
def add(x):
    return x + 1

def multiply(x):
    return x * 2

# Composición manual: se pasa la salida de `add` como entrada a `multiply`
def composed(x):
    return multiply(add(x))

print(composed(5))  # 12

```

## 7. Uso de Funciones de Orden Superior

Las funciones de orden superior son funciones que aceptan otras funciones como argumentos o devuelven funciones como resultados. Son fundamentales en la programación funcional, ya que permiten construir abstracciones reutilizables y modulares.

**Ejemplo: Filtrar números pares de una lista**
```python
def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

print(filter_even([1, 2, 3, 4, 5]))  # [2, 4]
```

> [!WARNING]
> Función lambda (muy parecida a arrow function de JS). Útil cuando se necesita una función rápida y sencilla sin declararla explícitamente.

## 8. Ejemplo Completo en Python

**Ejemplo: Filtrar usuarios de una lista**
```python
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

# Filtrar usuarios mayores de 25, extraer sus nombres y transformarlos a mayúsculas
processed_users = list(
    map(
        lambda user: user["name"].upper(),
        filter(lambda user: user["age"] > 25, users)
    )
)

print(processed_users)  # ['BOB', 'CHARLIE']
```

## 9. Ventajas y Desventajas de la Programación Funcional

La programación funcional ofrece numerosos beneficios, pero también presenta ciertos desafíos. A continuación, se destacan las principales ventajas y desventajas.

---

### Ventajas

1. **Código más predecible**:
   - Las funciones puras siempre producen la misma salida para las mismas entradas, lo que facilita las pruebas y la depuración.

2. **Reutilización**:
   - Las funciones son modulares y reutilizables, lo que fomenta la creación de componentes pequeños y bien definidos.

3. **Menor riesgo de errores**:
   - La inmutabilidad evita errores relacionados con el estado mutable y los efectos colaterales. Además facilita la prueba (testing) del código

4. **Soporte para paralelismo**:
   - Dado que no hay datos mutables ni estado compartido, es más seguro ejecutar tareas en paralelo. 

5. **Declaratividad**:
   - El enfoque declarativo permite centrarse en el **qué** hacer, en lugar de **cómo** hacerlo, lo que mejora la legibilidad del código.

---

### Desventajas

1. **Curva de aprendizaje**:
   - El paradigma funcional puede ser menos intuitivo para quienes están acostumbrados a la programación imperativa u orientada a objetos.

2. **Rendimiento**:
   - La creación constante de nuevos datos en lugar de modificar estructuras existentes puede ser costosa en términos de memoria y CPU.

3. **Complejidad inicial**:
   - Conceptos como funciones de orden superior, composición e inmutabilidad pueden ser difíciles de entender para principiantes.

4. **Verboso en algunos casos**:
   - Resolver problemas simples puede requerir más código o abstracciones adicionales en comparación con otros paradigmas.

---

### Resumen

La programación funcional es ideal para resolver problemas de manera modular y escalable, especialmente en entornos donde la inmutabilidad y la ausencia de efectos secundarios son críticas. Sin embargo, puede no ser la mejor elección en contextos que requieren un enfoque imperativo o altamente optimizado para rendimiento.

🚨 ¿Qué es la programación imperativa? 🚨

## 10. Recursos Adicionales

Si quieres profundizar en la programación funcional, aquí tienes algunos recursos recomendados:

---

### Libros y Documentación

- **[Functional Programming in Python (O'Reilly)](https://www.oreilly.com/library/view/functional-python-programming/9781784396992/)**
  - Un libro completo sobre cómo aplicar la programación funcional en Python.
- **[Real Python: Functional Programming](https://realpython.com/python-functional-programming/)**
  - Una guía detallada con ejemplos prácticos de programación funcional en Python.
- **[Python.org: Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)**
  - Una introducción oficial a la programación funcional en Python.

---

### Herramientas y Librerías

- **[`functools`](https://docs.python.org/3/library/functools.html)**
  - Un módulo estándar de Python con herramientas útiles para la programación funcional. Ejemplo partial crea una nueva función a partir de otra, fijando algunos de sus argumentos o reduce

---

### Proyectos Práctico

1. **Procesamiento de texto**:
   - Realiza transformaciones funcionales como convertir palabras a mayúsculas, contar frecuencias y filtrar palabras clave siguiendo el paradigma funcional

2. **Transformación de datos JSON**:
   - Aplica funciones puras para filtrar y mapear datos de archivos JSON siguiendo el paradigma funcional

