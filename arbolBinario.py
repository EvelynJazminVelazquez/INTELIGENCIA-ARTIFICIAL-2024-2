# Crear nodos como diccionarios
nodo_raiz = {'dato': 6, 'izquierdo': None, 'derecho': None}
nodo_izquierdo = {'dato': 4, 'izquierdo': None, 'derecho': None}
nodo_derecho = {'dato': 8, 'izquierdo': None, 'derecho': None}

# Enlazar los nodos
nodo_raiz['izquierdo'] = nodo_izquierdo  # El nodo izquierdo del nodo raíz es 4
nodo_raiz['derecho'] = nodo_derecho  # El nodo derecho del nodo raíz es 8

# Función para mostrar los nodos en un recorrido "in-order" (izquierdo, raíz, derecho)
def recorrido_in_order(nodo):
    if nodo is not None:
        recorrido_in_order(nodo['izquierdo'])  # Recorrer el subárbol izquierdo
        print(nodo['dato'], end=" ")  # Imprimir el nodo actual
        recorrido_in_order(nodo['derecho'])  # Recorrer el subárbol derecho

# Mostrar el árbol con un recorrido in-order
recorrido_in_order(nodo_raiz)
