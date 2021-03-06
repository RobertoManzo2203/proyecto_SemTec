import cv2
import numpy as np


def maxPooling(Ioriginal):
    filas = len(Ioriginal)//2
    columnas = len(Ioriginal[0])//2

    matrizresultado = np.zeros((filas, columnas), np.uint8) #matríz resultado

    for i in range(0,filas):
        for j in range(0,columnas):
            matrizresultado[i][j] = np.max(Ioriginal[i*2:i*2+2, j*2:j*2+2])
    return matrizresultado
   
def convolucion(Ioriginal, kernel):
    fr = len(Ioriginal)-(len(kernel)-1)
    cr = len(Ioriginal[0])-(len(kernel[0])-1)
    res = np.zeros((fr, cr), np.uint8)
    
    for i in range(len(res)):
        for j in range(len(res[0])):
            suma = 0
            for m in range(len(kernel)):
                for n in range(len(kernel[0])):
                    suma += kernel[m][n] * Ioriginal[m+i][n+j]
            if suma<=255:
                res[i][j]=round(suma)
            else:
                res[i][j]=255

    return res

nombreimagen = input('Nombre de la imagen')
IRGB = cv2.imread(nombreimagen)

IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
k1 = 1/256*np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,2,1]]) 
IGS = convolucion(IGS, k1)
IGS = maxPooling(IGS)
k2 = np.array([[2,2,4,2,2],[1,1,2,1,1],[0,0,0,0,0],[-1,-1,-2,-1,-1],[-2,-2,-4,-2,-2]]) 
IGS = convolucion(IGS, k2)
IGS = maxPooling(IGS)
nuevonombre = nombreimagen[0:nombreimagen.find(".")]+'b'+nombreimagen[nombreimagen.find("."):]
cv2.imwrite(nuevonombre, IGS)

