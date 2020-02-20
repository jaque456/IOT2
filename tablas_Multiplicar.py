# Tablas de multiplicar


def TablasMultiplicación(Numeros):
    Maximo = 10
    Result = 1

    while Result <= Maximo:
        resultado = Result* Numeros

        print("{} x {} = {}".format(Numeros, Result, resultado))

        Result = Result + 1

TablasMultiplicación(10)
