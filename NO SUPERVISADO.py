import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Datos simulados: Coordenadas (x, y) de las estaciones
estaciones = {
    "Portal Norte": [10, 50],
    "Calle 85": [15, 45],
    "Calle 100": [20, 40],
    "Calle 72": [25, 35],
    "Calle 26": [30, 30],
    "Tercer Milenio": [35, 25],
    "Avenida Jiménez": [40, 20],
    "Museo Nacional": [45, 15],
    "Portal Sur": [50, 10],
    "Portal Américas": [55, 5],
}

# Convertir a array para clustering
nombres_estaciones = list(estaciones.keys())
coordenadas = np.array(list(estaciones.values()))

# Algoritmo de clustering K-Means
num_clusters = 3  # Número de grupos
modelo_kmeans = KMeans(n_clusters=num_clusters, random_state=0)
modelo_kmeans.fit(coordenadas)

# Etiquetas de los clusters
etiquetas = modelo_kmeans.labels_

# Visualizar resultados
def visualizar_clusters(coordenadas, etiquetas, nombres_estaciones):
    plt.figure(figsize=(10, 7))
    colores = ['red', 'blue', 'green', 'purple', 'orange']
    
    for i, nombre in enumerate(nombres_estaciones):
        plt.scatter(coordenadas[i, 0], coordenadas[i, 1], color=colores[etiquetas[i]], label=nombre)
        plt.text(coordenadas[i, 0] + 1, coordenadas[i, 1] + 1, nombre, fontsize=9)
    
    # Mostrar centroides
    centroides = modelo_kmeans.cluster_centers_
    plt.scatter(centroides[:, 0], centroides[:, 1], color="black", marker="x", s=100, label="Centroides")
    
    plt.title("Clustering de estaciones (TransMilenio)")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.legend(loc="upper right", fontsize=8)
    plt.grid(True)
    plt.show()

visualizar_clusters(coordenadas, etiquetas, nombres_estaciones)