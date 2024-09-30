import networkx as nx

# Creamos un grafo dirigido, usando la libreria networkx
G = nx.Graph()

# Agregamos nodos y arcos (con pesos como el tiempo de viaje para poder realizar los calculos de nuestro trayecto)
edges = [
    ('A', 'B', 5),
    ('A', 'C', 10), #Esta ruta no es rentable en nuestro ejemplo, así que no se toma
    ('B', 'C', 2),
    ('B', 'D', 4), #Esta ruta tampoco es rentable en nuestro ejemplo, así que no se toma
    ('C', 'D', 1),
    ('D', 'E', 3),
]

# Ahora agregamos los arcos al grafo, esto con el fin de crear la estructura de red que usaremos para encontrar las rutas
G.add_weighted_edges_from(edges)

# Usar Dijkstra dentro de la función "encontrar_mejor_ruta" para encontrar la ruta más corta
def encontrar_mejor_ruta(graph, inicio, fin):
#Esto nos devuelve la ruta más corta como una lista de nodos
    ruta = nx.dijkstra_path(graph, inicio, fin)
#Este nos devuelve el costo total (peso) de esa ruta
    costo = nx.dijkstra_path_length(graph, inicio, fin)
    return ruta, costo

# Dentro de "evaluar_reglas" vamos a definir reglas lógicas que serán añadidas al proceso
def evaluar_reglas(ruta):
    reglas = [
        {'ruta': ['A', 'B'], 'condicion': 'Evitar_A'},
        {'ruta': ['C', 'D'], 'condicion': 'Horario_Pico'},
    ]
    
    decisiones = []
#Recorremos nuestro arreglo de reglas
    for regla in reglas:
#Si se cumple una de las reglas, la añadimos con "append" a nuestro resultado
        if regla['ruta'] in [ruta[i:i+2] for i in range(len(ruta) - 1)]:
            decisiones.append(f"Regla aplicada: {regla['condicion']}")
    
    return decisiones
#Inicio de nuestra aplicación, aca podemos añadir prints para debuggear, tambien podemos cambiar nuestro "inicio" y "fin" para hacer pruebas con otras rutas
def main():
    inicio = 'A'
    fin = 'E'
    ruta, costo = encontrar_mejor_ruta(G, inicio, fin)
    decisiones = evaluar_reglas(ruta)
#Empezamos a armar la respuesta de nuestro proceso
    print(f"Ruta óptima: {' -> '.join(ruta)}")
    print(f"Costo: {costo}")
    for decision in decisiones:
        print(decision)

if __name__ == "__main__":
    main()
