# -*- coding: cp1252 -*-
from PIL import Image
from funciones import *
import numpy as np
import os
import sys

def abrirArchivo(nombreArchivo):
	if sys.platform == 'linux2':
    		subprocess.call(["xdg-open", nombreArchivo])
	else:
    		os.startfile(nombreArchivo)

def ArrayAImagen(arr, nombreSalida):
	im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
	im.save(nombreSalida)
	abrirArchivo(nombreSalida)
	return True

def sepia(arreglo,contador):
            matriztemp = arreglo.tolist()
            for pixely in range(len(matriztemp)):
                        for pixelx in range(len(matriztemp[pixely])):
                                red, green, blue = matriztemp[pixely][pixelx]
                                newred =(red * 0.393) + (green * 0.769) + (blue * 0.189))
                                newgreen =(red * 0.349) + (green * 0.686) + (blue * 0.168))
                                newblue =(red * 0.272) + (green * 0.534) + (blue * 0.131))
                                if newred > 254:
                                        newred = 255
                                if newgreen > 254:
                                        newgreen = 255
                                if newblue > 254:
                                        newblue = 255
                                matriztemp[pixely][pixelx] = [newred, newgreen, newblue]
            salida = nombre+str(contador)+".png"
            arreglo = np.array(matriztemp)
            ArrayAImagen(arreglo, salida)
            contador += 1
            return arreglo, contador

def espejovertical(arreglo, contador):
	arreglo = np.array(arreglo)[::-1]
	salida = nombre+str(contador)+".png"
	ArrayAImagen(arreglo, salida)
	contador += 1
	return arreglo, contador

def espejo(arreglo, contador):
    arreglo = np.fliplr(arreglo)
    salida = nombre+str(contador)+".png"
    ArrayAImagen(arreglo, salida)
    contador += 1
    return arreglo, contador
    

def  escaladeMrgrey (arreglo, contador):
	matriztemp = arreglo.tolist()
	for pixely in range(len(matriztemp)):
		for pixelx in range(len(matriztemp[pixely])):
			red, green, blue = matriztemp[pixely][pixelx]
			gris = (red+green+blue)/3
			valorRGBnew = [gris, gris, gris]
			matriztemp[pixely][pixelx] = valorRGBnew
	salida = nombre+str(contador)+".png"
	arreglo = np.array(matriztemp)
	ArrayAImagen(arreglo, salida)
	contador += 1
	return arreglo, contador

def rotar(arreglo, contador, rotacion):	#1=90[grado],2=180[grado],3=270[grado]
	arreglo = numpy.rot90(arreglo,rotacion)
	salida = nombre+str(contador)+".png"
	ArrayAImagen(arreglo, salida)
	contador += 1
	return arreglo, contador


def negativo(arreglo, contador):
    matriz1 = arreglo.tolist()
    for filaPix in matriz1:
        for pix in filaPix:
            for color in range(3):
                pix[color] = 255 - pix[color]
    arreglo = np.array(matriz1)
    salida = nombre+str(contador)+".png"
    ArrayAImagen(arreglo, salida)
    contador +=1
    return arreglo, contador
    
def pixelado(matriz, tamanopxl):
	tamanopxl = int(tamañopxl)
	promediopxl = 0
	if (len(matriz%tamañopxl != 0) and len(matriz[0] != 0):
		print 'ingrese un tamaño de pixel compatible con su imagen'

	else:
		for pixely in range(len(matriz))[::tamanopxl]:
			for pixelx in range(len(matriz[pixely]))[::tamanopxl]:
				prom = promediocolores(matriz, pixely, pixelx,promediopxl, tamanopxl)
				aplicarcolor (matriz, promediopxl,tamanopxl)
	return
				

def promediocolores (matriz, pixely, pixelx, promediopxl, tamanopxl):
	for y in range(tamañopxl):
		red, green, blue = matriz[pixely+y][pixelx]
		promediopxl += (red+green+blue)/3
		for x in range(tamañopxl):
			red, green, blue = matriz[pixely][pixelx+x]
			promediopxl += (red+green+blue)/3
	promediopxl = promediopxl/tamanopxl
	return promediopxl

def aplicarcolor (matriz, promediopxl,tamanopxl):
	for y in range(tamañopxl):
		red, green, blue = matriz[pixely+y][pixelx]
		red, green, blue = promediopxl, promediopxl, promediopxl
		for x in range(tamañopxl):
			red, green, blue = matriz[pixely][pixelx+x]
			red, green, blue = promediopxl, promediopxl, promediopxl
	return None

nombre = raw_input("Ingrese el nombre de la imagen: ")
tipo = "."+raw_input("Ingrese el tipo de archivo de la imagen: ")
imagen = nombre+tipo
archivo = nombre + ".txt"
convertirImagenAArchivo(imagen, archivo)
matriz = leerArchivo(archivo)
arreglo = np.array(matriz)
contador = 1
flag = True
dic = {"espejo": espejo,
       "espejovertical": espejovertical,
       "edg": escaladeMrgrey,
       "negativo": negativo,
       "sepia": sepia}
       
while flag:
    fleg = True
    print "Comandos disponibles:\nsepia: Aplica efecto sepia a la imagen\nespejo : Aplica efecto espejo a la imagen\nespejovertical : Aplica efecto de espejo vertical a la imagen\nedg : Aplica efecto de escala de grises a la imagen\nnegativo: Aplica efecto negativo a la imagen\n90 : Rota la Imagen en 90º\n180: Rota la imagen en 180º\n270 : Rota la imagen en 270º"
    comando = raw_input("Ingrese un comando: ").lower()
    if comando == "" or comando not in ["espejo", "espejovertical", "edg", "negativo", "90", "180", "270", "sepia"]:
        print "Por favor, ingrese un comando valido"
    else:
        if comando in ["90","180","270"]:
            arreglo, contador = rotar(arreglo, contador, int(comando)/90)
        else:
            arreglo, contador = dic[comando](arreglo, contador)
        while fleg:
            asd = raw_input("Desea realizar otra operacion? (s/n): ").lower()
            if asd not in ["s","n"] or asd == '':
                print "Ingrese un comando valido"
            else:
                fleg = False
                if asd == "n":
                    flag = False
                    ArrayAImagen(arreglo, nombre+"Final.png")
