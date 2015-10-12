#Importar funciones para Graficar
import numpy as np
import matplotlib.pyplot as plt

#Funcion que retorna un dic que contiene la frecuencia de cada palabra en el parrafo
def histoParrafo(parrafo):
    #Eliminar Signos de Puntuacion
    for punt in [',','.','#',';','$','%','&','\/','(',')','=','\"','\'']:
        parrafo = parrafo.replace(punt,'')
    #Convertir a Minuscula, eliminar \n y volver una lista el parrafo
    palabras = parrafo.lower().strip().split()
    #Crear Histograma en un diccionario
    histograma = {}
    for palabra in palabras:
        if palabra not in histograma.keys():
            histograma[palabra] = palabras.count(palabra)
            tpl = (palabra, histograma[palabra])
            histo01.append(tpl)
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

#Funcion que calcula la distancia Coseno de dos Histogramas
def distCoseno(histograma1,histograma2):
    #Guarda las distancias Euclidianas de ambos histogramas
    distE1 = distEuclidiana(histograma1,{})
    distE2 = distEuclidiana(histograma2,{})
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

histo01 = []
a = raw_input("Ingrese nombre archivo 1 aqui (Sin .txt): ")
b = raw_input("Ingrese nombre archivo 2 aqui (Sin .txt): ")
archivo1 = open(a + '.txt')
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
        archivo2 = open(b + '.txt')
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
                
                if porcentaje > 50:                          #Si el porcentaje es mayor a 50, se agrega a la lista de parrafos en conflicto
                    conflictos.append((nParr1,nParr2,porcentaje))
                    porcentajes.append(porcentaje)
    archivo2.close()
archivo1.close()

if len(porcentajes) > 1:
    print "Los parrafos en conflicto son:"
    for i in conflictos:
        parra1, parra2, porcen = i
        print "Los parrafos", str(parra1), "y", str(parra2), "con un", str(porcen),"% de similitud."
    plt.title("Frecuencia de porcentajes de similitud entre parrafos en conflicto")
    plt.grid(True)
    plt.hist(porcentajes)
    plt.xlabel("Porcentajes")
    plt.ylabel("Frecuencia")
    plt.show()
else:
    print "No hay parrafos en conflicto"
