import math
print('dame 10 numeros')
lista=[]
total=0
for i in range(10):
    valor=int(input("Ingrese un valor entero:"))
    while valor%2==0:
        valor=int(input("no es impar, prueba de nuevo:"))
    lista.append(valor)
    total+=valor
print(lista) #lista
print(total," es el sumatorio de la lista") #sumatorio
print(total/i," es la media de la lista") #media