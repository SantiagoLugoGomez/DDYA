#Santiago Lugo ejercicio diagnostico
def pedirNum(msg):

    num = int(input(msg))
    return num


def positivoNegativo(num, texto):

    if num > 0:
        print(texto, "es positivo")

    elif num < 0:
        print(texto, "es negativo")

    else:
        print(texto, "es cero")


def fibonacci(num, texto):

    a = 0
    b = 1
    encontrado = False

    while a <= num:

        if a == num:
            encontrado = True

        c = a + b
        a = b
        b = c

    if encontrado:
        print(texto, "pertenece a la secuencia de Fibonacci")

    else:
        print(texto, "NO pertenece a la secuencia de Fibonacci")


def primo(num, texto):

    if num < 2:

        print(texto, "NO es primo")

    else:

        primo = True
        x = 2

        while x < num:

            if num % x == 0:

                primo = False

            x += 1

        if primo:

            print(texto, "es primo")

        else:

            print(texto, "NO es primo")


def intermedios(num1, num2):

    if num1 < 0 and num2 < 0:

        multi = 1

        if num1 < num2:

            for i in range(num1 + 1, num2):

                multi *= i

        elif num2 < num1:

            for i in range(num2 + 1, num1):

                multi *= i

        else:

            print("No existen números intermedios")
            return

        print("La multiplicación de los números intermedios es:", multi)

    else:

        suma = 0

        if num1 < num2:

            for i in range(num1 + 1, num2):

                suma += i

        elif num2 < num1:

            for i in range(num2 + 1, num1):

                suma += i

        else:

            print("No existen números intermedios")
            return

        print("La suma de los números intermedios es:", suma)


def parImpar(num, texto):

    if num % 2 == 0:

        print(texto, "elevado al cubo es:", num ** 3)

    else:

        print(texto, "elevado al cuadrado es:", num ** 2)


def codigoEstudiantil(codigo):

    print("Su código estudiantil es:", codigo)

    for x in codigo:

        print("Dígito:", x)


def main():

    print("Buenos días querido usuario.")

    num1 = pedirNum("Ingrese el primer número: ")
    num2 = pedirNum("Ingrese el segundo número: ")

    positivoNegativo(num1, "El primer número")
    fibonacci(num1, "El primer número")
    primo(num1, "El primer número")

    print("--------------------------")

    positivoNegativo(num2, "El segundo número")
    fibonacci(num2, "El segundo número")
    primo(num2, "El segundo número")

    print("--------------------------")

    intermedios(num1, num2)

    print("--------------------------")

    parImpar(num1, "El primer número")
    parImpar(num2, "El segundo número")

    print("--------------------------")

    codigo = input("Ingrese su código estudiantil: ")

    codigoEstudiantil(codigo)
    print("Punto 8: lo que haria seria pedir el dia/mes y año del estudiante junto con su codigo estudiantil,compararia el numero con el mes, ejemplo 1=enero y al final pondria el dia/mes en letras y año+ el codigo estudiantil , realmente no me acuerdo de esa función, probe con un if y no me funcionaba")
    print("Punto 9: lo que haria con mi pensamiento logico es pedir una letra y compararla con las cinco vocales, si coincide con ellas imprimo que es vocal sino imprimo que es una consonante, como lo dije anteriormente no me acordaba de si podia usar un while o un if entonces para no engañarme pongo que realmente el codigo no me funcionaba en este punto, por errores propios de sintaxis")
    print("Punto 10: este punto fue el que mas me costo y por eso considero que esta en el numero 10,realmennte no sabia una solución por cuenta propia, asi que investigue y le pregunte a la IA como lo hubiera hecho y me respondio esto:el abecedario tiene 27 letras,recorrer el abecedario desde la A hasta la Z,comparar la letra ingresada con cada letra del abecedario y mostrar la posición de la letra en el abecedario")
    print("Muchas gracias por su tiempo y confiar en mi programa querido usuario, feliz día")
main()