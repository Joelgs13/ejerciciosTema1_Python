# Crea una clase Criptográfo que contenga dos métodos: encriptar y desencriptar. Los dos
# métodos recibirán un texto y devolverán otro texto. El funcionamiento de los métodos es el
# siguiente:
# ◦ encriptar(txt): El texto recibido se encriptará sustituyendo cada uno de los
# caracteres por el siguiente caracter según su valor ASCII.
# ◦ desencriptar(txt): Realizará la acción inversa al metodo anterior, es decir sustituirá
# cada carácter por el anterior según su valor ASCII.
# Nota: Para realizar este ejercicio son muy útiles las funciones ord() y chr().

class Criptografo:
    def encriptar(texto):
        devolver=""
        for caracter in texto:
            devolver+=str(ord(caracter))+' '
        return devolver
    def desencriptar(texto):
        devolver = ""
        caracteres = texto.split()  
        for valor in caracteres:
            devolver += chr(int(valor))  
        return devolver
    
cr1 = Criptografo
print(cr1.encriptar(input("Dame texto a encriptar: ")))
print(cr1.desencriptar(input("Dame texto para desencriptar: ")))