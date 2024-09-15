# Crear nodos como diccionarios
nodo1 = {'dato': 6, 'siguiente': None}
nodo2 = {'dato': 1, 'siguiente': None}
nodo3 = {'dato': 9, 'siguiente': None}

# Enlazar los nodos
nodo1['siguiente'] = nodo2  # nodo1 apunta a nodo2
nodo2['siguiente'] = nodo3  # nodo2 apunta a nodo3

# Función para recorrer la lista y mostrar los elementos
def mostrar_lista(nodo):
    actual = nodo
    while actual is not None:  # Mientras el nodo actual exista
        print(actual['dato'], end=" -> ")
        actual = actual['siguiente']
    print("None")

# Mostrar la lista enlazada
mostrar_lista(nodo1)
