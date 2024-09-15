# Función de ordenamiento burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambiar los elementos si están en el orden incorrecto
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:")
print(lista)

burbuja(lista)

print("Lista ordenada:")
print(lista)
