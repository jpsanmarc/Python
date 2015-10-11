#Importar funciones para Graficar
##from matplotlib import hist, show
import os

#Funcion que retorna un dic que contiene la frecuencia de cada palabra en el parrafo
def histoParrafo(parrafo):
    palabras = parrafo.strip().split()
    histograma = {}
    for palabra in palabras:
        if palabra not in histograma.keys():
            histograma[palabra] = palabras.count(palabra)
    return histograma

#Retorna un conjunto con todas las palabras de ambos parrafos y completa los histogramas con las palabras que no aparecen en los parrafos
def vocabulario(histograma1,histograma2):
    vocab = set()
    for palabra in histograma1:
        vocab.add(palabra)
    for palabra in histograma2:
        vocab.add(palabra)
    return vocab

#Funcion que calcula la distancia euclidiana a partir de los diccionarios con las frecuencias de las palabras. Usar diccionario vacio para deu(h1,0)
def distEuclidiana(histograma1, histograma2):
    #Obtener conjunto con todas las palabras
    vocab = vocabulario(histograma1, histograma2)
    #Sumar la cantidad de palabras diferentes
    suma = 0
    for palabra in vocab:
        #Cantidad de Veces que esta la palabra en el Histograma 1
        if palabra not in histograma1:
            palabraR1 = 0
        else:
            palabraR1 = histograma1[palabra]
        #Cantidad de Veces que esta la palabra en el Histograma 1
        if palabra not in histograma2:
            palabraR2 = 0
        else:
            palabraR2 = histograma2[palabra]
        suma += (palabraR1 - palabraR2) ** 2
    return suma ** 0.5

def deu0(hist):                                  ##Distancia euclidiana para un valor y 0
    suma = 0
    for valor in hist.values():
        suma += valor**2
    return suma**0.5

#Funcion que calcula la distancia Coseno de dos Histogramas
def distCoseno(histograma1,histograma2):
    #Guarda las distancias Euclidianas de ambos histogramas
    distE1 = deu0(histograma1)
    distE2 = deu0(histograma2)    
    suma = 0
    vocab = vocabulario(histograma1, histograma2)
    for palabra in vocab:
        #Cantidad de Veces que esta la palabra en el Histograma 1
        if palabra not in histograma1:
            palabraR1 = 0
        else:
            palabraR1 = histograma1[palabra]
        #Cantidad de Veces que esta la palabra en el Histograma 1
        if palabra not in histograma2:
            palabraR2 = 0
        else:
            palabraR2 = histograma2[palabra]
        suma += palabraR1 * palabraR2
    return abs(round(1 - (suma/(distE1*distE2)),12))

a = raw_input("Ingrese nombre archivo 1 aqui: ")
b = raw_input("Ingrese nombre archivo 2 aqui: ")
archivo1 = open(a)
pt1 = 0                               ##Numero del parrafo del texto 1
distancias = []
for parrafo in archivo1:
    if parrafo != "\n":               ##Comprueba que el parrafo no sea solo un salto de linea
        pt1 += 1                      ## Cada vez que pasa por este punto, cambia de parrafo y se le suma 1 al parrafo actual
        dic1 = histoParrafo(parrafo)
        archivo2 = open(b)
        pt2 = 0                       ##Numero del parrafo del texto 2
        for parrafo2 in archivo2:
            if parrafo2 != "\n":      ##Comprueba que el parrafo no sea solo un salto de linea
                pt2 += 1              ## Cada vez que pasa por este punto, cambia de parrafo y se le suma 1 al parrafo actual
                dic2 = histoParrafo(parrafo2)
                dist1 = distEuclidiana(dic1, dic2)
                dist2 = distCoseno(dic1, dic2)
                distancias.append((pt1, pt2, dist1, dist2))
for i in distancias:
    print '-----------------'
    apt1, apt2, adist1, adist2 = i
    print apt1, '-', apt2
    print 'Euc:', adist1
    print 'Cos:', adist2
    

