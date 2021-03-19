import numpy as np
import cv2

#Ioriginal = matriz original
def convolucion(Ioriginal,Kernel):
     '''Método encargado de realizar una convolución a una imagen
        Entrada:
        Ioriginal - imagen original en forma de matríz
        kernel - kernel para barrer la imagen
        Salida:
        res - imagen resultante'''
    #fr - filas, cr - columnas
    fr=len(Ioriginal)-(len(Kernel)-1)
    cr=len(Ioriginal[0])-(len(Kernel[0])-1)
    Resultado=np.zeros((fr,cr),np.uint8)
    
    #filas, matríz resultado
    for i in range(len(Resultado)):
        #columnas, matríz resultado
        for j in range(len(Resultado[0])):
            suma=0
            #filas, kernel
            for m in range(len(Kernel)):
                #columnas, kernel
                for n in range(len(Kernel[0])):
                    suma+=Kernel[m][n]*Ioriginal[m+i][n+j]
            if suma<=255:        
                Resultado[i][j]=round(suma)
            else:
                Resultado[i][j]=255
    return Resultado
#imagenes
K=[[-1,0,1],[-1,0,1],[-1,0,1]] #kernel
I=[[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]] #prototipo de imagen

#imagenes a numpy arrays
In=np.array(I)
Kn=np.array(K)

IRGB=cv2.imread('004.jpg')
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS.shape)

#funcion de convolucion
R=convolucion(IGS,Kn)
print(R)
print(R.shape)
cv2.imwrite('004C.jpg',R)			#columnas, kernel
				for n in range(len(kernel[0])):
					suma += kernel[m][n] * Ioriginal[m+i][n+j]
			res[i][j] = suma
	return res

K = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]] #kernel
I = [[2, 0, 1, 1, 1], [3, 0, 0, 0, 2], [1, 1, 1, 1, 1], [3, 1, 1, 1, 2], [1, 1, 1, 1, 1]] #prototipo de imagen

#conversión de arrays a numpy arrays
In = np.array(I)
Kn = np.array(K)

#llamado de la función e impresion del resultado
R = convolucion(In, Kn)
print(R)
