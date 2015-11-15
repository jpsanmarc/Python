from PIL import Image
from funciones import *
import numpy as np
import os

def ArrayAImagen(arr, nombreSalida):
	im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
	im.save(nombreSalida)
	return True

def espejovertical(matriz):
	espejo = np.array(matriz)[::-1]
	salida = nombre+"espejovertical"+tipo
	ArrayAImagen(espejo, salida)
	os.system(salida)
	
def espejo(matriz):
    espejo = np.array(matriz)
    espejo = np.fliplr(espejo)
    salida = nombre+"espejo"+tipo
    ArrayAImagen(espejo, salida)
    os.system(salida)

def  escaladeMrgrey (matriz):
	for pixely in matriz:
		for pixelx in pixely:
			red, green, blue = pixelx[pixely][0]
			gris = (red+green+blue)/3
			valorRGBnew = [gris, gris, gris]
			pixely[pixelx] = valorRGBnew

def rotar(imagenMatriz, rotacion):	#1=90[grado],2=180[grado],3=270[grado]
	imagenMatriz = numpy.rot90(numpy.array(imagenMatriz),rotacion).tolist()
	convertirMatrizAImagen(imagenMatriz, 'yummy.png')

def negativo(matriz):
	for filaPix in matriz:
		for pix in filaPix:
			for color in range(3):
				pix[color] = 255 - pix[color]



while True:
	nombre = raw_input("Ingrese el nombre de la imagen: ")
	tipo = raw_input("Ingrese el tipo de archivo de la imagen(inclyendo punto): ")
	imagen = nombre+tipo
	archivo = nombre + ".txt"
	convertirImagenAArchivo(imagen, archivo)
	matriz = leerArchivo(archivo)
	print 'las acciones posibles son: "pixelado", "escala de gris","espejo", "espejo vertical", "rotar",  "negativo" y "salir"'
	prompt1 = raw_input(' ¿Que desea hacer con el archivo? (escritas como aparecen más arriba)')
	
	if prompt1 == 'pixelado':
		size = raw_input('¿Que tamanio desea que tenga cada pixel resultante?')
		pixelado(matriz, size)
		
	elif prompt1 == 'escala de gris':
		escaladeMrgrey(matriz)
		
	elif prompt1 == 'espejo':
		espejo(matriz)
		
	elif prompt1 == 'espejo vertical':
		espejovertical(matriz)

	elif prompt1 == 'rotar':
		rota = raw_input('¿Por que angulo quiere rotar la imagen? (Puede ser por 90,180, 270, 360)')
		rota = rota/90
		rotar(matriz, rota)
		
	elif prompt1 == 'negativo':
		negativo(matriz)
	elif prompt1 == 'salir':
		break
	else:
		print 'ingrese una opcion valida'

a = raw_input()



