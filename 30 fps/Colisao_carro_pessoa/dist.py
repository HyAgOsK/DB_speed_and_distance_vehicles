import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df_model = pd.read_csv('dist_person_car.csv')
df_real = pd.read_csv('car_person_pos.csv')

yolo_dist = df_model["distancia"]

distancias = []


# Agrupa por frame
for frame, grupo in df_real.groupby("Frame"):
    if len(grupo) == 2:
        obj1 = grupo.iloc[0]
        obj2 = grupo.iloc[1]

        # Posição dos objetos
        p1 = np.array([obj1["PosX"], obj1["PosY"], obj1["PosZ"]])
        p2 = np.array([obj2["PosX"], obj2["PosY"], obj2["PosZ"]])

        # Calcula a distância Euclidiana
        distancia = np.linalg.norm(p1 - p2)

        # Armazena o resultado
        distancias.append(distancia)

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

# Convertendo distancias para array do numpy (caso ainda seja uma lista)
distancias = np.array(distancias)

# Garantindo que ambos os arrays tenham o mesmo tamanho
min_len = min(len(yolo_dist), len(distancias))
yolo_dist = yolo_dist[:min_len]
distancias = distancias[:min_len]

# Cálculo dos erros
mae = np.mean(np.abs(yolo_dist - distancias))
mse = np.mean((yolo_dist - distancias) ** 2)
rmse = np.sqrt(mse)
mape = np.mean(np.abs((yolo_dist - distancias) / distancias)) * 100

# Exibindo resultados
print(f"MAE:  {mae:.4f}")
print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAPE: {mape:.2f}%")

# Garantindo que ambos os arrays tenham o mesmo tamanho
min_len = min(len(yolo_dist), len(distancias))
yolo_dist = yolo_dist[:min_len]
distancias = np.array(distancias[:min_len])  # Garante que distancias é um np.array

# Calculando estatísticas
stats_yolo = calculate_statistics(yolo_dist)
stats_real = calculate_statistics(distancias)

# Exibindo resultados
print("\nEstatísticas - Distância YOLO:")
for k, v in stats_yolo.items():
    print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")

print("\nEstatísticas - Distância Real:")
for k, v in stats_real.items():
    print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")


# # Calculando estatísticas
# yolo_stats = calculate_statistics(yolo_dist)
#
# # Exibindo estatísticas
# print("Estatísticas - Distância Real:")
# for k, v in real_stats.items():
#     print(f"{k}: {v:.4f}")
# print()
#
# print("Estatísticas - Distância YOLO:")
# for k, v in yolo_stats.items():
#     print(f"{k}: {v:.4f}")
# print()

# Plotando os gráficos comparativos
plt.figure(figsize=(10, 4))
plt.plot(distancias, label='Real distance', color='red', linestyle='--', linewidth=2)
plt.plot(yolo_dist, label='Measured distance', color='blue')
plt.title(" ")
plt.xlabel("")
plt.ylabel("Distance (m)")
plt.legend()
plt.grid(True)
plt.show()
