# Calcular factorial
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)


# calcular productoria
def calcular_productoria(productorias):
    producto = 1
    for numero in productorias:
        producto *= numero
    return producto


# ingreso de operaciones
def ingreso_operaciones(**argumentos):
    for operacion, valor in argumentos.items():
        if "fact_" in operacion:
            resultado = calcular_factorial(valor)
            print(f"El factorial de {valor} es {resultado}")
        elif "prod_" in operacion:
            resultado = calcular_productoria(valor)
            print(f"La productoria de {valor} es {resultado}")
        else:
            print(
                'Argumento incorrecto, por favor ingresar "fact_(numero)" para calcular factorial y "prod_(numero)" para productoria'
            )


# Ejemplo
print(ingreso_operaciones(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6))
