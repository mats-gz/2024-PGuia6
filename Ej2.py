import random
numMult = random.randint(1, 10)
archivo_texto = f"tabla-{numMult}.txt"

try:

    with open(archivo_texto, "r") as archivo:
        tablas = archivo.read()
        print(tablas)

except FileNotFoundError:
    print(f"El archivo '{archivo_texto}' no fue encontrado.")

except IOError:
    print(f"No se pudo abrir el archivo '{archivo_texto}'.")