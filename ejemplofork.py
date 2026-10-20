"""Calculadora basica con menu.

Permite capturar dos numeros y realizar las operaciones de suma,
resta, multiplicacion, division y potencia.
"""

# "Debes corregir este error, vale mia"

MENU = (
    "Seleccione una opcion:\n"
    "1--> Capturar numeros\n"
    "2--> Sumar\n"
    "3--> Restar\n"
    "4--> Multiplicar\n"
    "5--> Dividir\n"
    "6--> Potencia\n"
    "0--> Salir"
)

# "Aca esta perfecto"

def parar():
    """Detiene el programa hasta que el usuario presione ENTER."""
    input("Presione <la tecla> para continuar")


def capturar_numero(mensaje):
    """Solicita un numero al usuario.

    Retorna el valor como float, o None si el dato no es valido.
    """
    try:
        return float(input(mensaje))
    except ValueError:
        print("El dato digitado no es un numero valido")
        return None


def sumar(a, b):
    """Retorna a + b."""
    return a + b


def restar(a, b):
    """Retorna a - b."""
    return a - b


def multiplicar(a, b):
    """Retorna a * b."""
    return a * b


def dividir(a, b):
    """Retorna a / b, o None si b es cero."""
    if b == 0:
        return None
    return a / b


def potencia(a, b):
    """Retorna a elevado al valor b."""
    return a ** b


def mostrar_resultado(a, simbolo, b, resultado):
    """Muestra el resultado de una operacion."""
    if resultado is None:
        print("No es posible dividir entre cero")
    else:
        print(f"{a} {simbolo} {b} = {resultado}")
    parar()
    

def main():
    """Muestra el menu y ejecuta la opcion seleccionada."""
    a = 0.0
    b = 0.0
    continuar = True

    while continuar:
        opcion = input(MENU + "\n")

        if opcion == "1":
            nuevo_a = capturar_numero("Digite el primer numero: ")
            nuevo_b = capturar_numero("Digite el segundo numero: ")
            if nuevo_a is not None and nuevo_b is not None:
                a, b = nuevo_a, nuevo_b
        elif opcion == "2":
            mostrar_resultado(a, "+", b, sumar(a, b))
        elif opcion == "3":
            mostrar_resultado(a, "-", b, restar(a, b))
        elif opcion == "4":
            mostrar_resultado(a, "*", b, multiplicar(a, b))
        elif opcion == "5":
            mostrar_resultado(a, "/", b, dividir(a, b))
        elif opcion == "6":
            mostrar_resultado(a, "**", b, potencia(a, b))
        elif opcion == "0":
            print("Bye")
            continuar = False
        else:
            print("Seleccione una opcion valida")

if __name__ == "__main__":
    main()
