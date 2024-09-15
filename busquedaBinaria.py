# Función para realizar búsqueda binaria
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Encuentra el índice medio

        if lista[medio] == objetivo:
            return medio  # Elemento encontrado, retorna el índice
        elif lista[medio] < objetivo:
            inicio = medio + 1  # Busca en la mitad derecha
        else:
            fin = medio - 1  # Busca en la mitad izquierda

    return -1  # Elemento no encontrado

# Lista ordenada
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Buscar un elemento en la lista
elemento_buscado = 9
resultado = busqueda_binaria(lista_ordenada, elemento_buscado)

if resultado != -1:
    print(f"Elemento {elemento_buscado} encontrado en el índice {resultado}.")
else:
    print(f"Elemento {elemento_buscado} no encontrado en la lista.")
