
# Crear una cola vacía
cola = []

# Encolar (agregar al final de la cola)
def encolar(cola, elemento):
    cola.append(elemento)
    print(f"Encolado: {elemento}")

# Desencolar (eliminar del frente de la cola)
def desencolar(cola):
    if len(cola) > 0:
        elemento = cola.pop(0)
        print(f"Desencolado: {elemento}")
        return elemento
    else:
        print("La cola está vacía")
        return None

# Ver si la cola está vacía
def cola_vacia(cola):
    return len(cola) == 0

# Mostrar el contenido de la cola
def mostrar_cola(cola):
    print("Contenido de la cola:", cola)

# Ejemplo de uso
encolar(cola, 10)
encolar(cola, 20)
encolar(cola, 30)
mostrar_cola(cola)

desencolar(cola)
mostrar_cola(cola)

desencolar(cola)
mostrar_cola(cola)

desencolar(cola)
mostrar_cola(cola)

desencolar(cola)  # Intentar desencolar cuando está vacía


