# Algoritmos de Búsqueda 🔍

Estos programas fueron creados durante clases del [Curso de Introducción al Pensamiento Computacional con Python de Platzi](https://platzi.com/cursos/python-cs/ "Curso de Introducción al Pensamiento Computacional con Python de Platzi").  💚

Son algoritmos que buscan la raíz cuadradas de un número.

Ejecutar en su entorno favorito con Python3.

## Funcionamiento de cada algoritmo

### Enumeración exhaustiva (enumeracion.py)

Este algoritmo busca todas las posibles respuestas enumerando del 1 a la posible respuesta comparando si ese número**2 es igual al número ingresado(objetivo).

Sólo dará respuesta si existe raíz cuadrada exacta.

### Aproximación Numérica (aproximacion.py)

Busca la raíz cuadrada mendiante aproximaciones en pasos sumando un valor epsilon**2, donde epsilon es nuestro margen de error.

La respuesta será una aproximación no exacta. Este algoritmo no es tan eficiente. Al reducir su margen de error el tiempo de búsqueda crece exponencialmente.

### Búsqueda binaria (busqueda_binaria.py)

Aplica *divide and conquer*, separando la busqueda en mitades de todo el recorrido que tendría que hacer en la enumeración. Para ello asigna un límite inferior y superior en cada iteración para reducir la búsqueda a un rango menor de números.

Este algoritmo solo funciona para enumeraciones ordenadas, pero es más eficiente y rápido.

### programas_numericos.py

Este script es una recopilación donde puedes escoger cualquiera de los tres algoritmos. Está dividido en funciones.

