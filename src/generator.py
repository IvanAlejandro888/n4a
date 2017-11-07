#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Ivan Alejandro

    Este es un simple generador de palabras basado en azar
'''

from random import randint
import sys

silabas = []

valoresTotales = []
listaPalabras = {}
listaOrdenada = {}

tbc = {
    'a': 12.53,
    'b': 1.42,
    'c': 4.68,
    'd': 5.86,
    'e': 13.68,
    'f': 0.69,
    'g': 1.01,
    'h': 0.70,
    'i': 6.25,
    'j': 0.44,
    'k': 0.02,
    'l': 4.97,
    'm': 3.15,
    'n': 6.71,
    'ñ': 0.31,
    'o': 0.68,
    'p': 2.51,
    'q': 0.88,
    'r': 6.87,
    's': 7.98,
    't': 4.63,
    'u': 3.93,
    'ü': 0.001,
    'v': 0.90,
    'w': 0.01,
    'x': 0.22,
    'y': 0.90,
    'z': 0.52
}

def getSilabas():
    sil = open('../data/silabas.txt', 'r')
    for silaba in sil:
        silabas.append(silaba.strip())
    sil.close()

def getRandomSilaba():
    return silabas[randint(0, len(silabas)-1)]

def testSilaba(silaba):
    result = 100.0

    ac = ''
    an = ''

    for i in list(silaba):
        ac = i

        if ac is not an:
            result -= tbc[ac]

        an = ac
    return result

def testPalabra(word):
    result = 0.0

    ac = ''
    an = ''

    for i in list(word):
        ac = i

        if ac is not an:
            result += tbc[ac]

        an = ac

    return result

# Funciones de ejecución

def run(size, silength, length):
    palabra = ''
    act = ''

    # Numero de silabas
    for i in range(size):
        competencia = []
        valor = {}

        # Generacion de silabas
        for j in range(length):
            si = getRandomSilaba()

            while True:
                if len(si) > silength:
                    si = getRandomSilaba()
                else:
                    break

            competencia.append(testSilaba(si))
            valor[testSilaba(si)] = si

        # Eleccion de silaba

        act = valor[float(min(competencia))]
        palabra += act

    # Palabra formada completamente

    valoresTotales.append(testPalabra(palabra))
    listaPalabras[testPalabra(palabra)] = palabra

def ordenar(lista, diccionario):
    lista2 = list(lista)
    lista3 = lista2.sort(reverse=True)
    final = {}

    for i in lista3:
        final[i] = diccionario[i]

    return final

# Parte de ejecución

getSilabas()

## test()

if(sys.argv[1] == '--help'):
    print(
        "ARG1 -> Exigencia de la eleccion de silabas\n" +
        "ARG2 -> Longitud maxima de cada silaba\n" +
        "ARG3 -> Cuantas silabas va a tener cada palabra\n" +
        "ARG4 -> Cuantas palabras aleatorias se van a generar"
    )
else:

    # Numero de palabras
    for i in range(int(sys.argv[4])):
        run(int(sys.argv[3]), int(sys.argv[2]), int(sys.argv[1]))
    
    # Sorting (imposible desde funcion)

    for key in sorted(listaPalabras, reverse=True):
        print('> ' + str(listaPalabras[key]))