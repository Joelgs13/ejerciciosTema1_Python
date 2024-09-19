from ejercicio7 import Persona


def main():
    p1 = Persona(nombre="Carlos", edad=17, sexo="H", peso=90, altura=1.74)
    p2 = Persona(nombre="Jeff", edad=41, sexo="H", peso=80, altura=1.91)
    p3 = Persona(nombre="Claudia", edad=19, sexo="M", peso=70, altura=1.63)

    personas = [p1, p2, p3]

    def estado_peso(persona):
        imc = persona.calcularIMC()
        if imc == Persona.PESOBAJO:
            print(f"{persona.nombre} está por debajo del peso ideal")
        elif imc == Persona.PESOIDEAL:
            print(f"{persona.nombre} está en su peso ideal")
        else:
            print(f"{persona.nombre} tiene sobrepeso")

    def estado_edad(persona):
        if persona.esMayorDeEdad():
            print(f"{persona.nombre} es mayor de edad")
        else:
            print(f"{persona.nombre} es menor de edad")

    for persona in personas:
        estado_peso(persona)
        estado_edad(persona)
        print(persona) 

if __name__ == "__main__":
    main()
