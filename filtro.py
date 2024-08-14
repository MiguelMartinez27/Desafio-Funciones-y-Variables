import sys

# Diccionario precios
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

#filtracion
def filtrar_productos(umbral, condicion="mayor"):
    if condicion == "mayor":
        productos_filtrados = {producto:precio for producto, precio in precios.items() if precio > umbral}
    elif condicion == "menor":
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    else:
        return "Lo sentimos, no es una operación válida"
    
    return productos_filtrados

# Verificación de argumentos
if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    productos = filtrar_productos(umbral)
    print(f"Los productos mayores al umbral son: {', '.join(productos.keys())}")

elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    condicion = sys.argv[2]
    productos = filtrar_productos(umbral, condicion)
    
    if condicion == "mayor":
            print(f"Los productos mayores al umbral son: {', '.join(productos.keys())}")
    elif condicion == "menor":
            print(f"Los productos menores al umbral son: {', '.join(productos.keys())}")

else:
    print("Lo sentimos, no es una operación válida")
