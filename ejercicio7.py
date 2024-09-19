"""7. Haz una clase llamada Persona que siga las siguientes condiciones:
 Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura.
No queremos que se accedan directamente a ellos. Si quieres añadir algún atributo
puedes hacerlo.
 Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo
(0 números, cadena vacía para String, etc.). Sexo sera hombre por defecto, usa una
constante para ello.
 Los métodos que se implementaran son:
 calcularIMC(): calculara si la persona esta en su peso ideal (peso en
kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la
función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos),
significa que esta por debajo de su peso ideal la función devuelve un 0 y si
devuelve un valor mayor que 25 significa que tiene sobrepeso, la función
devuelve un 1. Te recomiendo que uses constantes para devolver estos
valores.
 esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
 toString(): devuelve toda la información del objeto.
 generaDNI(): genera un número aleatorio de 8 cifras, genera a partir de este
su número su letra correspondiente. Este método sera invocado cuando se
construya el objeto. Puedes dividir el método para que te sea más fácil. No
será visible al exterior.
 Métodos set de cada parámetro, excepto de DNI"""

import random

class Persona:
    # Constantes para el IMC
    PESOBAJO = -1
    PESOIDEAL = 0
    SOBREPESO = 1

    def __init__(self, nombre="", edad=0, sexo="H", peso=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.__dni = self.__generaDNI()
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    # Método para calcular el IMC
    def calcularIMC(self):
        if self.altura <= 0:
            raise ValueError("La altura debe ser mayor a 0.")
        imc = self.peso / (self.altura ** 2)
        if imc < 20:
            return self.PESOBAJO
        elif 20 <= imc <= 25:
            return self.PESOIDEAL
        else:
            return self.SOBREPESO

    def esMayorDeEdad(self):
        return self.edad >= 18

    # Método para generar el DNI (privado)
    def __generaDNI(self):
        numero_dni = random.randint(10000000, 99999999)
        letra = self.__calculaLetraDNI(numero_dni)
        return f"{numero_dni}{letra}"

    # Método auxiliar para calcular la letra del DNI (privado)
    def __calculaLetraDNI(self, numero):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        return letras[numero % 23]

    def toString(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, "
                f"Peso: {self.peso}kg, Altura: {self.altura}m, DNI: {self.__dni}")

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        if sexo in ["H", "M"]:
            self.sexo = sexo
        else:
            raise ValueError("El sexo debe ser 'H' (hombre) o 'M' (mujer)")

    def setPeso(self, peso):
        self.peso = peso

    def setAltura(self, altura):
        self.altura = altura
