
# -*- coding: cp1252 -*-
from PIL import Image
from funciones import *
import numpy as np
import os
import sys
import subprocess

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
            newred = (red * 0.393) + (green * 0.769) + (blue * 0.189)
            newgreen = (red * 0.349) + (green * 0.686) + (blue * 0.168)
            newblue = (red * 0.272) + (green * 0.534) + (blue * 0.131)
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

def rotar(arreglo, contador, rotacion): #1=90[grado],2=180[grado],3=270[grado]
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
'''
def promediarPixeles(pixeles):
    sumaR, sumaG, sumaB = 0, 0, 0
    total = len(pixeles)
    for pix in pixeles:
        sumaR += pix[0]
        sumaG += pix[1]
        sumaB += pix[2]
    prom = [sumaR/total,sumaG/total,sumaB/total]
    return prom


def pixelado(imagenMatriz,tamanioPixel):
    lenY = len(imagenMatriz)
    lenX = len(imagenMatriz[0])
    print lenX, lenY
    inicio = [0,0]
    for i in range(lenX * lenY):
        pixeles = list()
        pos = list()
        for fila in range(tamanioPixel):
            if inicio[0] + fila == lenY:
                break
            for col in range(tamanioPixel):
                if inicio[1] + col == lenX:
                    break
                filaR, colR = inicio[0]+fila,inicio[1]+col
                #print filaR, colR
                print lenY, ':', filaR
                print lenX, ':', colR
                pixeles.append(imagenMatriz[filaR][colR])
                pos.append((filaR,colR))
            inicio[1] += tamanioPixel
            print inicio[1]
        inicio[0] += tamanioPixel
        inicio[1] = 0
        prom = promediarPixeles(pixeles)
        for pix in pos:
            imagenMatriz[pix[0]][pix[1]] = prom
    return imagenMatriz
'''

def tonalizar(arreglo, contador):
    color = raw_input('Ingrese el color al que desea tonalizar (R:Rojo,G:Verde,B:Azul): ')
    matriz = arreglo.tolist()
    for pixely in range(len(matriz)):
        for pixelx in range(len(matriz[pixely])):
            if color.lower() == 'r':
                matriz[pixely][pixelx][0] = 255
            elif color.lower() == 'g':
                matriz[pixely][pixelx][1] = 255
            elif color.lower() == 'b':
                matriz[pixely][pixelx][2] = 255
            else:
                print 'Abortando accion...\nPor favor ingrese solo la letra R, G o B'
                return False
    salida = nombre+"Tonalizar.png"
    arreglo = np.array(matriz)
    ArrayAImagen(arreglo, salida)
    contador += 1
    return arreglo, contador

## Interaccion con el Usuario ##

os.system("clear")
flag = True
while flag:
    nombre = raw_input("Ingrese el nombre de la imagen (Sin extension): ")
    tipo = "." + raw_input("Ingrese el tipo de archivo de la imagen: ")
    imagen = nombre + tipo
    if os.path.isfile(imagen):
        flag = False
    else:
        os.system("clear")
        print 'Este archivo no existe, ingrese otro nombre.'
archivo = nombre + ".txt"
print 'Convirtiendo imagen a archivo...'
convertirImagenAArchivo(imagen, archivo)
print 'Importando archivo a matriz...'
matriz = leerArchivo(archivo)
arreglo = np.array(matriz)
contador = 1

filtros  = {"espejo":espejo,
            "espejovertical":espejovertical,
            "edg":escaladeMrgrey,
            "negativo":negativo,
            "90":rotar,
            "180":rotar,
            "270":rotar,
            "sepia":sepia,
            "tonalizar":tonalizar
            }

comandos = {"espejo":"Aplica efecto espejo.",
            "espejovertical":"Aplica efecto de espejo vertical.",
            "edg":"Aplica efecto de escala de grises.",
            "negativo":"Aplica efecto negativo a la imagen.",
            "90":"Rota la imagen en 90°.",
            "180":"Rota la imagen en 180°.",
            "270":"Rota la imagen en 270°.",
            "sepia":"Aplica efecto sepia.",
            "tonalizar":"Intensifica un color en especifico (Rojo, Azul o Verde)."
            }

flag = True
while flag:
    fleg = True
    os.system("clear")
    print "Comandos Disponibles:"                                           #Imprimir comandos Disponibles
    for comando in comandos:
        print '     ' + comando + ': ' + comandos[comando]
    comando = raw_input("Ingrese un comando: ").lower()                     #Ingresar comando
    if comando == "" or comando not in comandos.keys():                     #Validacion
        os.system("clear")
        print "Por favor, ingrese un comando valido"
    else:
        if comando in ["90","180","270"]:                                   #Comando de Rotar
            arreglo, contador = rotar(arreglo, contador, int(comando)/90)
        else:
            arreglo, contador = filtros[comando](arreglo, contador)
        while fleg:
            confirmacion = raw_input("Desea realizar otra operacion? (s/n): ").lower()
            if confirmacion not in ["s","n"] or confirmacion == '':
                print "Ingrese solo s o n"
            else:
                fleg = False
            if confirmacion == "n":
                flag = False
                ArrayAImagen(arreglo, nombre+"Final.png")
                os.system("clear")
