import random
numMult = random.randint(1, 10)
archivo_texto = f"tabla-{numMult}.txt"

numAux = 1
tabla = []
while (10 >= numAux):
    multNum = numMult * numAux
    cadNums = f"{numMult} x {numAux} = {multNum}"
    tabla.append(cadNums)
    numAux += 1

print(tabla)

try:
    
    with open(archivo_texto, 'w') as archivo:
        for num in tabla:
            archivo.write(f"{num} \n")
            
except IOError:
    print(f"No se pudo abrir el archivo '{archivo_texto}' en modo escritura.")