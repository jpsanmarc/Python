#Importar funciones para Graficar
import numpy as np
import matplotlib.pyplot as plt

#Funcion que retorna un dic que contiene la frecuencia de cada palabra en el parrafo
def histoParrafo(parrafo):
    palabras = parrafo.strip().split()
    histograma = {}
    for palabra in palabras:
    if palabra not in histograma.keys():
        histograma[palabra] = palabras.count(palabra)
        tpl = (palabra, histograma[palabra])
        global histo01.append(tpl)
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
nParr1 = 0                               ##Permite saber que parrafo se esta revisando del Archivo 1
distanciasE = {}
distanciasC = {}
conflictos = []
Euclid = np.array([])
Coseno = np.array([])
porcentajes = []
for parrafo1 in archivo1:
    if parrafo1 != "\n":               ##Comprueba que el parrafo no sea solo un salto de linea
        nParr1 += 1
        histo1 = histoParrafo(parrafo1)
        archivo2 = open(b)
        nParr2 = 0                       ##Permite saber que parrafo se esta revisando del Archivo 1
        for parrafo2 in archivo2:
            if parrafo2 != "\n":      ##Comprueba que el parrafo no sea solo un salto de linea
                nParr2 += 1
                histo2 = histoParrafo(parrafo2)
                distE = distEuclidiana(histo1, histo2) #Distancia Euclidiana entre Parrafo1 y Parrafo2
                distC = distCoseno(histo1, histo2) #Distancia Coseno entre Parrafo1 y Parrafo2
                distanciasE[(nParr1,nParr2)] = distE
                distanciasC[(nParr1,nParr2)] = distC
                porcentaje = 100 - (round(distC,2) * 100)    #Calcula porcentaje de similitud entre ambos parrafos
                porcentajes.append(porcentaje)
                if porcentaje > 50:                          #Si el porcentaje es mayor a 50, se agrega a la lista de parrafos en conflicto
                    conflictos.append((nParr1,nParr2,porcentaje))

print "Los parrafos en conflicto son:"
for i in conflictos:
    parra1, parra2, porcen = i
    print "Los parrafos", str(parra1), "y", str(parra2), "con un", str(porcen),"% de similitud."

#Grafica
tablaC = np.array([[1,2,3],[3,4,5],[5,6,6]])
tablaE = np.array([[1,2],[3,4],[5,6]])
print tablaC
plt.title("Frecuencia de porcentajes de similitud entre parrafos")
plt.grid(True)
plt.plot(tablaC)
plt.show()

