import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lendo os arquivos CSV
data2 = pd.read_csv("blender-dataset/homography_transform.csv")

id_counts_2 = data2['ID do Carro'].value_counts()
most_common_id_2 = id_counts_2.idxmax()


# Extraindo as velocidades para o ID com mais aparições no primeiro arquivo
velocities_id_2 = data2[data2['ID do Carro'] == most_common_id_2]['Velocidade (km/h)'].values.tolist()


# Função para calcular estatísticas
def calculate_statistics(velocities):
    statistics = {
        'mean': np.mean(velocities),
        'median': np.median(velocities),
        'std_dev': np.std(velocities),
        'max': np.max(velocities),
        'min': np.min(velocities),
        'count': len(velocities)
    }
    return statistics

# Calculando estatísticas para as duas listas de velocidades
stats_id_2 = calculate_statistics(velocities_id_2)

# Resultados
print(f'Estatísticas para o ID {most_common_id_2} no arquivo homography:')
print(stats_id_2)

# Gerando o gráfico
plt.figure(figsize=(12, 6))

#plt.plot(velocities_id_1, label='(simple)')
plt.plot(velocities_id_2, label='(hg)')

# Adicionando detalhes ao gráfico
plt.title('Comparação de métodos de cálculo de velocidade')
plt.xlabel('Frames')
plt.ylabel('Velocidade (km/h)')
plt.legend()
plt.grid()


# Exibindo o gráfico
plt.show()
