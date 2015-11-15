# -*- coding: cp1252 -*-
from PIL import Image
from funciones import *
import numpy as np
import os

def ArrayAImagen(arr, nombreSalida):
	im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
	im.save(nombreSalida)
	os.system(nombreSalida)
	return True

def espejovertical(matriz):
	espejov = np.array(matriz)[::-1]
	salida = nombre+"EspejoVertical.png"
	ArrayAImagen(espejov, salida)

def espejo(matriz):
    espejo = np.array(matriz)
    espejo = np.fliplr(espejo)
    salida = nombre+"Espejo.png"
    ArrayAImagen(espejo, salida)
    

def  escaladeMrgrey (matriz):
	for pixely in range(len(matriz)):
		for pixelx in range(len(matriz[pixely])):
			red, green, blue = matriz[pixely][pixelx]
			gris = (red+green+blue)/3
			valorRGBnew = [gris, gris, gris]
			matriz[pixely][pixelx] = valorRGBnew
			os.system(salida)

def rotar(imagenMatriz, rotacion):	#1=90[grado],2=180[grado],3=270[grado]
	imagenMatriz = numpy.rot90(numpy.array(imagenMatriz),rotacion)
	salida = nombre+"Rotacion"+str(rotacion*90)+".png"
	ArrayAImagen(imagenMatriz, salida)


def negativo(matriz):
    matriz1 = matriz
    for filaPix in matriz1:
        for pix in filaPix:
            for color in range(3):
                pix[color] = 255 - pix[color]
    salida = nombre+"Negativo.png"
    convertirMatrizAImagen(matriz1, salida)
    os.system(salida)

nombre = raw_input("Ingrese el nombre de la imagen (sin extension) : ")
tipo = "."+raw_input("Ingrese el tipo de archivo de la imagen: ")
imagen = nombre+tipo
archivo = nombre + ".txt"
convertirImagenAArchivo(imagen, archivo)
matriz = leerArchivo(archivo)
flag = True
dic = {"espejo": espejo,
       "espejovertical": espejovertical,
       "edg": escaladeMrgrey,
       "negativo": negativo}
       
while flag:
    fleg = True
    print "Comandos disponibles:\nespejo : Aplica efecto espejo a la imagen\nespejovertical : Aplica efecto de espejo vertical a la imagen\nedg : Aplica efecto de escala de grises a la imagen\nnegativo: Aplica efecto negativo a la imagen\n90 : Rota la Imagen en 90º\n180: Rota la imagen en 180º\n270 : Rota la imagen en 270º"
    comando = raw_input("Ingrese un comando: ").lower()
    if comando == "" or comando not in ["espejo", "espejovertical", "edg", "negativo", "90", "180", "270"]:
        print "Por favor, ingrese un comando valido"
    else:
        if comando in ["90","180","270"]:
            rotar(matriz, int(comando)/90)
        else:
            dic[comando](matriz)
        while fleg:
            asd = raw_input("Desea realizar otra operacion? (s/n): ").lower()
            if asd not in ["s","n"] or asd == '':
                print "Ingrese un comando valido"
            else:
                fleg = False
                if asd == "n":
                    flag = False
        
'''
while True:
	nombre = raw_input("Ingrese el nombre de la imagen: ")
	tipo = raw_input("Ingrese el tipo de archivo de la imagen(inclyendo punto): ")
	imagen = nombre+tipo
	archivo = nombre + ".txt"
	convertirImagenAArchivo(imagen, archivo)
	matriz = leerArchivo(archivo)
	print 'las acciones posibles son: "pixelado", "escala de gris","espejo", "espejo vertical", "rotar",  "negativo" y "salir"'
	prompt1 = raw_input(' Que desea hacer con el archivo? (escritas como aparecen mas arriba)')
	
	if prompt1 == 'pixelado':
		size = raw_input('Que tamanio desea que tenga cada pixel resultante?')
		pixelado(matriz, size)
		
	elif prompt1 == 'escala de gris':
		escaladeMrgrey(matriz)
		
	elif prompt1 == 'espejo':
		espejo(matriz)
		
	elif prompt1 == 'espejo vertical':
		espejovertical(matriz)

	elif prompt1 == 'rotar':
		rota = raw_input('Por que angulo quiere rotar la imagen? (Puede ser por 90,180, 270, 360)')
		rota = rota/90
		rotar(matriz, rota)
		
	elif prompt1 == 'negativo':
		negativo(matriz)
	elif prompt1 == 'salir':
		break
	else:
		print 'ingrese una opcion valida'

a = raw_input()
'''
    
