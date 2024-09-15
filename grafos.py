# Crear el grafo como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función para mostrar el grafo
def mostrar_grafo(grafo):
    for nodo in grafo:
        print(f"Nodo {nodo} está conectado a: {', '.join(grafo[nodo])}")

# Mostrar el grafo
mostrar_grafo(grafo)
