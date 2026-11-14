# Cálculo lambda

El cálculo lambda es un sistema formal que Alonzo Church desarrolló en la década de 1930 para estudiar las funciones y expresar computaciones. Es una de las bases teóricas de la programación funcional.

Esta guía usa ejemplos de Python para entender las ideas. Python y el cálculo lambda **no son lo mismo**: Python incluye números, cadenas y operaciones como `+`, que no existen como elementos predefinidos en el cálculo lambda puro.

## 1. Los tres elementos

Las expresiones del cálculo lambda se construyen con:

1. **Variables**, como `x`.
2. **Abstracciones**, que definen funciones. `λx.M` significa «una función que recibe `x` y devuelve la expresión `M`».
3. **Aplicaciones**, que aplican una función a un argumento. Se escriben `M N`.

Por ejemplo, `λx.x` es la **función identidad**: recibe un valor y devuelve ese mismo valor. Aplicada a `a`, se escribe:

```text
(λx.x) a → a
```

En Python, podemos expresar la misma idea así:

```python
identidad = lambda x: x

print(identidad(5))       # 5
print(identidad("hola"))  # hola
```

`lambda x: x` define una función; `identidad(5)` la llama con el argumento `5`. En Python, `lambda` permite definir funciones cuyo cuerpo es una sola expresión.

## 2. Conversión alfa: cambiar el nombre de una variable

En cálculo lambda, el nombre de un parámetro no cambia lo que hace la función. Estas dos expresiones representan la misma función identidad:

```text
λx.x
λa.a
```

Cambiar el nombre de una variable ligada de esta forma se llama **conversión alfa**. Hay que cambiar sus usos de manera consistente y evitar conflictos con otras variables.

En Python, estas funciones calculan lo mismo cuando las llamamos con argumentos posicionales:

```python
def suma(x, y):
    return x + y

def agregar(a, b):
    return a + b

print(suma(20, 50))     # 70
print(agregar(20, 50))  # 70
```

En un programa, los nombres siguen siendo importantes para encontrar y llamar a las funciones: si cambiamos `suma` por otro nombre, debemos actualizar sus usos. Además, los nombres de los parámetros importan al pasar argumentos por nombre: `suma(x=20, y=50)` funciona, pero `agregar(x=20, y=50)` no.

## 3. Reducción beta: aplicar una función

La **reducción beta** explica cómo se aplica una función: sustituimos su parámetro por el argumento en el cuerpo, evitando conflictos con otras variables.

```text
(λx.x) a → a
```

Una analogía sencilla en Python:

```python
print((lambda x: x + " Jorge")("hola"))  # hola Jorge
```

La función recibe `"hola"` como `x`. Si sustituimos `x` en la expresión, obtenemos `"hola" + " Jorge"`, cuyo resultado es `"hola Jorge"`.

La concatenación de cadenas es una operación de Python, no del cálculo lambda puro. Esta sustitución es una forma intuitiva de entender el ejemplo, no una descripción completa de cómo Python evalúa todas las llamadas.

## 4. Currificación: una función que devuelve otra

En el cálculo lambda, cada función recibe **un argumento**. Para expresar una operación con dos argumentos, podemos crear una función que recibe el primero y devuelve otra función que recibe el segundo:

```text
λx.λy.x + y

((λx.λy.x + y) 20) 50 → 20 + 50 → 70
```

Aquí los números y `+` son una notación abreviada: en el cálculo lambda puro no están predefinidos, aunque pueden representarse mediante funciones.

La misma idea en Python se conoce como **currificación**:

```python
suma = lambda x: lambda y: x + y

print(suma(20)(50))  # 70
```

Paso a paso:

1. `suma(20)` devuelve una función que recuerda el valor `20`.
2. `(50)` llama a esa función con `y = 50`.
3. La función calcula `20 + 50` y devuelve `70`.

Podemos guardar la función intermedia y reutilizarla:

```python
suma = lambda x: lambda y: x + y

sumar_20 = suma(20)
print(sumar_20(50))  # 70
print(sumar_20(3))   # 23
```

También se puede escribir con `def`, usando funciones anidadas:

```python
def suma(x):
    def sumar(y):
        return x + y
    return sumar

print(suma(20)(50))  # 70
```

La idea se puede extender a tres argumentos:

```python
sumar_tres = lambda x: lambda y: lambda z: x + y + z

print(sumar_tres(1)(2)(3))  # 6
```

## 5. Relación con la programación funcional

Estos ejemplos muestran ideas importantes de la programación funcional: definir funciones, aplicarlas y devolver funciones desde otras funciones. La currificación permite crear funciones más específicas, como `sumar_20`, a partir de otras más generales.

Usar `lambda` en Python no garantiza por sí solo que una función sea pura o que sus datos sean inmutables: eso depende de lo que haga la función y de los datos que utilice.

## Apunte histórico

Alonzo Church fue el supervisor doctoral de Alan Turing en Princeton. El cálculo lambda y la máquina de Turing son modelos distintos, pero ambos permiten estudiar formalmente qué significa computar.
