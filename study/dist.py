import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lendo os dados do arquivo CSV
distance_data = pd.read_csv("blender-dataset/distancias_carros.csv")


# Função para calcular estatísticas
def calculate_statistics(values):
    return {
        'mean': np.mean(values),
        'median': np.median(values),
        'std_dev': np.std(values),
        'max': np.max(values),
        'min': np.min(values),
        'count': len(values)
    }


# Função para filtrar dados, calcular estatísticas e plotar gráfico
def analyze_and_plot(data, id1, id2, expected_distance):
    # Filtrando os dados para os IDs especificados
    filtered_data = data[
        ((data["car1_id"] == id1) & (data["car2_id"] == id2)) |
        ((data["car1_id"] == id2) & (data["car2_id"] == id1))
        ]

    # Calculando estatísticas
    distances = filtered_data["distancia"]
    stats = calculate_statistics(distances)

    # Exibindo estatísticas
    print("Gráfico comparando a distância esperada com a distância aferida")
    for key, value in stats.items():
        print(f"{key}: {value}")
    print()

    # Plotando o gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(filtered_data["frame"], distances, label="Distância Medida", color="blue")
    plt.axhline(y=expected_distance, color="red", linestyle="--", label=f"Distância Esperada ({expected_distance}m)")
    plt.title(f"Gráfico comparando a distância esperada com a distância aferida ao longo dos frames")
    plt.xlabel("Frame")
    plt.ylabel("Distância (m)")
    plt.legend()
    plt.grid()
    plt.show()


# Analisando e plotando para os pares de IDs
analyze_and_plot(distance_data, 2, 3, expected_distance=5)
analyze_and_plot(distance_data, 2, 4, expected_distance=24)
analyze_and_plot(distance_data, 4, 7, expected_distance=11)
