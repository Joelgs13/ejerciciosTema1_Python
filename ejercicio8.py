from ejercicio7 import Persona


def main():
    p1 = Persona(nombre="Juan", edad=25, sexo="H", peso=70, altura=1.75)
    p2 = Persona(nombre="Jeff", edad=25, sexo="H", peso=70, altura=1.75)
    p3 = Persona(nombre="Claudia", edad=25, sexo="H", peso=70, altura=1.75)
    p1.calcularIMC()
    p2.calcularIMC()
    p3.calcularIMC()
    p1.esMayorDeEdad()
    p2.esMayorDeEdad()
    p3.esMayorDeEdad()
    p1.toString()
    p2.toString()
    p3.toString()