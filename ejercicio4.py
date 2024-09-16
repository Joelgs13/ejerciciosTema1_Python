# Ejercicios Python
# 4. Adapta y amplia el programa anterior para que una vez introducidos los 10 números
# impares, se muestre un menú en pantalla con 5 opciones:
# ¿Que desea hacer con la lista?
# 1. Sumatorio
# 2. Media
# 3. Máximo
# 4. Mínimo
# 0. Salir
# Y después muestre el resultado de la opción seleccionada.*/

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
    print(sum(lista)," es el sumatorio de la lista") #sumatorio
elif opcion==2:
#media
    print(sum(lista)/i," es la media de la lista") #media
elif opcion==3:
#maximo
    print(maximo," Es el maximo de la lista")
elif opcion==4:
#minimo
    print(minimo," Es el minimo de la lista")
elif opcion==5:
#exit
    print("Hasta luego, que tengas un bonito dia")
    exit()
else:
    print("opcion no reconocida")
print("este print solo sirve para comprobar que el programa no pasa por aqui con la opcion 5")