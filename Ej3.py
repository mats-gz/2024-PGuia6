import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print(num1,num2)
archivo_texto = f"tabla-{num1}.txt"

try:

    with open(archivo_texto, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if f"{num1} x {num2} = " in linea:
                print(linea)

except FileNotFoundError:
    print(f"El archivo '{archivo_texto}' no fue encontrado.")

except IOError:
    print(f"No se pudo abrir el archivo '{archivo_texto}'.")