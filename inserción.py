# Función de ordenamiento por inserción
def insercion(lista):
    # Recorre la lista desde el segundo elemento
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Desplaza los elementos de la lista que son mayores que la clave a una posición adelante
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        # Inserta el elemento en la posición correcta
        lista[j + 1] = clave

# Ejemplo de uso
lista = [12, 11, 13, 5, 6]

print("Lista original:")
print(lista)

insercion(lista)

print("Lista ordenada:")
print(lista)
