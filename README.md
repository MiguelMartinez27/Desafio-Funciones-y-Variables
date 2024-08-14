# Desafío - Estructuras de Datos y Funciones (I)
##### Desafío - Estructuras de Datos y Funciones (II) correspondiente al bootcamp fullstack python.
Este repositorio contiene los archivos para ejecutar "filtro.py", "velocidad.py" y "ong.py". estos incluyen el uso de datos y funciones en python.

## Requisitos para ejecutar
* Sistema operativo Windows, MacOS o Linux
* Python 3.12 o superior

## Programas

### 1.- Filtro

Este programa sirve para filtrar datos, especificamente productos y sus respectivos precios, ingresando un umbral de valor y si desean productos de mayor o menor valor

#### Ejecución
* Ejecutar por terminal filtro.py junto con los argumentos correspondientes, es decir el umbral de valor que quiera filtrar y "menor" o "mayor" (mayor por defecto en caso de
no ingresar este argumento:

El programa debe devolver los productos que son de mayor o menor valor de acuerdo al umbral indicado anteriormente.

#### Ejemplo:

sh

python filtro.py 30000 menor

Respuesta esperada:

Los productos menores al umbral son: Teclado, Mouse

### 2.- velocidad
Este programa cumple la funcion de entregar las velocidades (u otro numero) mayores al promedio en un array entregado, se entrega la ubicacion del dato en el array:
el array es 
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

#### Ejecución

* Ejecutar por terminal el archivo velocidad.py

#### Ejemplo

sh

python velocidad.py

Respuesta esperada:

[0, 2, 3, 6, 8, 9, 10, 13, 15, 17, 18, 19, 20, 22, 24, 29, 30, 31, 32, 34, 35, 36, 37, 41, 48, 52, 54, 56, 57, 58, 59]

### 3.- ONG

Este programa permite calcular factoriales y productoria de cualquier numero, se ingresa un valor numérico como argumento con el nombre fact_i cuando se requiera
calcular un factorial, y una lista como argumento prod_i cuando se requiera calcular una productoria. Cabe destacar que la función permite ingresar estos argumentos en
cualquier orden y en cualquier cantidad.
Para ingresar distintos valores se debe hacer a traves del codigo

#### Ejecución

ejecutar por terminal el programa

#### Ejemplo

sh

python ong.py

Respuesta esperada:

El factorial de 5 es 120
La productoria de [4, 6, 7, 4, 3] es 2016
El factorial de 6 es 720


## Autor

Miguel Martínez F.
