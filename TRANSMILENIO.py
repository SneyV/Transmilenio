import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
def crear_grafo_transmilenio():
    grafo = nx.DiGraph()
    conexiones = [
        ("Portal Norte", "Calle 85", "B23", 10),
        ("Calle 85", "Calle 100", "B23", 5),
        ("Calle 100", "Calle 72", "B23", 8),
        ("Calle 72", "Calle 26", "B23", 12),
        ("Calle 26", "Tercer Milenio", "C15", 7),
        ("Tercer Milenio", "Avenida Jiménez", "C15", 5),
        ("Avenida Jiménez", "Museo Nacional", "C15", 6),
        ("Museo Nacional", "Portal Sur", "C15", 25),
        ("Portal Sur", "Calle 26", "E44", 15),
        ("Portal Américas", "Banderas", "H50", 10),
        ("Banderas", "Marsella", "H50", 8),
        ("Marsella", "Calle 26", "H50", 12),
    ]
    for origen, destino, ruta, tiempo in conexiones:
        grafo.add_edge(origen, destino, ruta=ruta, tiempo=tiempo)
    return grafo

# Visualización del grafo
def visualizar_grafo(grafo, ruta=None):
    posicion = nx.spring_layout(grafo)  # Disposición de los nodos
    plt.figure(figsize=(12, 8))
    
    # Dibujar todos los nodos y conexiones
    nx.draw(grafo, posicion, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=10)

    # Etiquetas de rutas
    etiquetas_rutas = nx.get_edge_attributes(grafo, "ruta")
    nx.draw_networkx_edge_labels(grafo, posicion, edge_labels=etiquetas_rutas, font_size=8)

    # Si hay una ruta, resáltala
    if ruta:
        conexiones_ruta = [(ruta[i], ruta[i + 1]) for i in range(len(ruta) - 1)]
        nx.draw_networkx_edges(
            grafo,
            posicion,
            edgelist=conexiones_ruta,
            edge_color="red",
            width=2.5,
        )
    plt.title("Sistema TransMilenio")
    plt.show()

# Encontrar la mejor ruta
def encontrar_mejor_ruta(grafo, inicio, destino):
    try:
        camino = nx.shortest_path(grafo, source=inicio, target=destino, weight="tiempo")
        tiempo_total = nx.shortest_path_length(grafo, source=inicio, target=destino, weight="tiempo")
        rutas = [grafo[camino[i]][camino[i + 1]]["ruta"] for i in range(len(camino) - 1)]
        return camino, rutas, tiempo_total
    except nx.NetworkXNoPath:
        return None, None, None

# Programa principal
def main():
    print("¡Bienvenido al módulo de TransMilenio!")
    print("Este sistema le ayudará a encontrar la mejor ruta entre dos estaciones.\n")

    grafo = crear_grafo_transmilenio()

    print("Estaciones disponibles:")
    print(", ".join(grafo.nodes))

    # Solicitar las estaciones al usuario
    estacion_inicio = input("\nIngrese la estación donde se encuentra: ")
    estacion_destino = input("Ingrese la estación a donde desea ir: ")

    if estacion_inicio not in grafo.nodes or estacion_destino not in grafo.nodes:
        print("\nError: Una o ambas estaciones no existen en el sistema.")
        return

    # Buscar la mejor ruta
    camino, rutas, tiempo_total = encontrar_mejor_ruta(grafo, estacion_inicio, estacion_destino)

    if camino:
        print(f"\nLa mejor ruta desde {estacion_inicio} hasta {estacion_destino} es:")
        for i in range(len(camino) - 1):
            print(f"  {camino[i]} -> {camino[i + 1]} (Ruta: {rutas[i]})")
        print(f"Tiempo estimado: {tiempo_total} minutos.")
        
        # Visualizar la ruta
        visualizar_grafo(grafo, ruta=camino)
    else:
        print(f"\nNo se encontró una ruta entre {estacion_inicio} y {estacion_destino}.")

if __name__ == "__main__":
    main()






