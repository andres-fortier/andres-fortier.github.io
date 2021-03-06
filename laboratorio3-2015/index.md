---
layout: default
title: Laboratorio 3 - UTN - SMA - 2015
---

# Laboratorio de Programación 3 - UTN - SMA - 2015

## [Calendario Tentativo](material/CalendarioTentativo2doSemestre.pdf)

## Clases

### Clase 1
  * [Imagen de Pharo 3.0 con Ozono para linux](material/pharo3.0.zip)
  * [Transparencias](material/Clase01.pdf)
  * [Página de la herramienta Ozono](http://www.pdep.com.ar/Home/software/software-pharo/object-browser-ultima-version) (ver [manual](http://www.pdep.com.ar/Home/software/software-pharo/object-browser-ultima-version/ObjectBrowser-manual.pdf?attredirects=0))

### Clase 2
  * [Contador Ozono](material/contador.o3.zip)
  * [Transparencias](material/Clase02.pdf)

### Clase 3
  * Consulta de práctica

### Clase 4
  * [Caja de Ahorro Ozono](material/cajaAhorro.ob.zip)
  * [Transparencias](material/Clase04.pdf)

### Clase 5
  * [Transparencias](material/Clase05.pdf)

### Clase 6
  * Consulta P1, sin transparencias

### Clase 7
  * [Transparencias](material/Clase07.pdf)

### Clase 8
 * [Transparencias](material/Clase08.pdf)

### Clase 9
 * [Transparencias](material/Clase09.pdf)

### Clase 10
  * [Transparencias](material/Clase10.pdf)
  * Algunos playgrounds (en cada paso inspeccionar el resultado y la colección)

```smalltalk
numeros := Array new: 10.
numeros size.
numeros first.
numeros at: 1 put: 23.
numeros first.
numeros at: 1.
numeros add: 10.

numeros := #(1 2 6 89 9).
numeros do: [:numero | Transcript show: numero; cr].
numeros select: [:numero | numero > 3].
numeros collect: [:numero | numero ** 2].
```

```smalltalk
numeros := OrderedCollection new.
numeros size.
numeros isEmpty.
numeros add: 10.
numeros isEmpty.
numeros first.
numeros at: 1 put: 23.
numeros first.
numeros at: 1.
numeros addFirst: 3.
numeros add: 134.
numeros add: 33.
numeros do: [:numero | Transcript show: numero; cr].
numeros select: [:numero | numero > 3].
numeros collect: [:numero | numero ** 2].
```

```smalltalk
numeros := SortedCollection sortBlock: [:unNumero :otroNumero | unNumero > otroNumero].
numeros size.
numeros add: 10.
numeros first.
numeros at: 1 put: 23.
numeros add: 30.
numeros add: 15.
numeros add: 33.

numeros do: [:numero | Transcript show: numero; cr].
numeros select: [:numero | numero > 20].
numeros collect: [:numero | numero printString].
```

```smalltalk
numeros := Set new.
numeros add: 10; add: 20; add: 10; add: 5;  add: 10.
numeros add: 15.
numeros add: 33.

numeros do: [:numero | Transcript show: numero; cr].
numeros select: [:numero | numero > 10].
numeros collect: [:numero | numero ** 2].
``` 

```smalltalk
numeros := #(1 3 6 89 22 3 12 6 89).

numeros asOrderedCollection.
numeros asSet.
numeros asSortedCollection.

"Números sin repetir mayores a 10"
numeros asSet select: [:numero | numero > 10].

"Números sin repetir mayores a 10 ordenados de mayor a menor"
numeros := numeros asSet select: [:numero | numero > 10].
numeros asSortedCollection: [:unNumero :otroNumero | unNumero > otroNumero].

"Ordenar strings por su tamaño"
#('Programación' 'hola' 'apa' 'Laboratorio') asSortedCollection: [:unaPalabra :otraPalabra | unaPalabra size < otraPalabra size].

"Seleccionar las palabras cuyo tamaño sea menor a 5"
#('Programación' 'hola' 'apa' 'Laboratorio') select: [:palabra | palabra size < 5].

"Obtener la primera palabra cuyo tamaño sea menor a 5"
#('Programación' 'hola' 'apa' 'Laboratorio') detect: [:palabra | palabra size < 5].
```

### Clase 11
  * [Transparencias](material/Clase11.pdf)

### Clase 12
  * [Transparencias](material/Clase12.pdf)

### Clase 13
  * [Transparencias](material/Clase13.pdf)

### Clase 14
  * [Transparencias](material/Clase14.pdf)

### Clase 15
  * [Transparencias](material/Clase15.pdf)

### Clase 16
  * [Transparencias](material/Clase16.pdf)

### Clase 18
  * [Transparencias](material/Clase18.pdf)

### Clase 19
  * [Transparencias](material/Clase19.pdf)

### Clase 20
  * [Transparencias](material/Clase20.pdf)

### Clase 21
  * [Transparencias](material/Clase21.pdf)

### Clase 22
  * [Transparencias](material/Clase22.pdf)

### Clase 23
  * Consulta de práctica

### Clase 24
  * [Transparencias](material/Clase24.pdf)

## Prácticas
  * [Práctica1](material/Practica1.pdf)
  * [Práctica2](material/Practica2.pdf)
  * [Práctica3](material/Practica3.pdf)
  * [Práctica4](material/Practica4.pdf)
  * [Práctica5](material/Practica5.pdf)
