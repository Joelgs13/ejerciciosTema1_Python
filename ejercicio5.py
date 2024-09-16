# Modifica el programa anterior de forma que cada una de las funcionalidades del programa se
# ejecute mediante una función.

def sumatorio():
    print(sum(lista)," es el sumatorio de la lista") #sumatorio

def media():
    print(sum(lista)/i," es la media de la lista") #media

def valorMaximo():
    print(maximo," Es el maximo de la lista") #maximo

def valorMinimo():
    print(minimo," Es el minimo de la lista")

def salirDelPrograma():
    print("Hasta luego, que tengas un bonito dia")
    exit()

import math
print('dame 10 numeros')
lista=[]
maximo=0
minimo=99999
for i in range(10):
    valor=int(input("Ingrese un valor entero:"))
    while valor%2==0:
        valor=int(input("no es impar, prueba de nuevo:"))
    lista.append(valor)
    if valor>maximo:
        maximo=valor
    if valor<minimo:
        minimo=valor
print(lista) #lista
#menu
print('¿Que desea hacer con la lista? \n 1. Sumatorio \n 2. Media \n 3. Máximo \n 4. Mínimo \n 5. Salir ')
opcion = int(input())
int(opcion)
while opcion>5 or opcion<1:
    print('1. Sumatorio \n 2. Media \n 3. Máximo \n 4. Mínimo \n 5. Salir ')
    opcion = int(input())
    int(opcion)
if opcion==1:
#sumatorio
    sumatorio()
elif opcion==2:
#media
    media()
elif opcion==3:
#maximo
    valorMaximo()
elif opcion==4:
#minimo
    valorMinimo()
elif opcion==5:
#exit
    salirDelPrograma()
else:
    print("opcion no reconocida")
print("este print solo sirve para comprobar que el programa no pasa por aqui con la opcion 5")