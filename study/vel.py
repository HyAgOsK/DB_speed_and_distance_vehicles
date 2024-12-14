import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lendo os arquivos CSV
data = pd.read_csv("blender-dataset/homography_transform.csv")

# Mapeando os IDs para novos IDs únicos
id_mapping = {
    1: 20,
    2: 10,
    3: 5,
    4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2,
    10: 1, 11: 1, 12: 1
}

# Aplicando o mapeamento
data['ID do Carro'] = data['ID do Carro'].replace(id_mapping)

# Configurando os valores esperados para cada ID
expected_speeds = {
    20: 20,
    10: 10,
    5: 5,
    2: 2,
    1: 1
}

# Criando a figura e os subgráficos
fig, axes = plt.subplots(5, 1, figsize=(12, 20), sharex=False)

for i, (car_id, expected_speed) in enumerate(expected_speeds.items()):
    # Filtrando os dados para o ID atual
    filtered_data = data[data['ID do Carro'] == car_id]

    # Obtendo os limites do eixo X com base nos frames disponíveis
    x_min = filtered_data["Frame"].min()
    x_max = filtered_data["Frame"].max()

    # Plotando as velocidades medidas
    axes[i].plot(
        filtered_data["Frame"],
        filtered_data["Velocidade (km/h)"],
        label=f'Velocidade Medida (ID {car_id})',
        color='blue'
    )

    # Plotando a linha de referência (velocidade esperada)
    axes[i].axhline(
        y=expected_speed,
        color='red',
        linestyle='--',
        label=f'Velocidade Esperada ({expected_speed} km/h)'
    )

    # Ajustando os limites do eixo X
    axes[i].set_xlim(x_min, x_max)

    # Configurando o título e os rótulos
    axes[i].set_title(f'Velocidade Medida vs Esperada para ID {car_id}')
    axes[i].set_ylabel('Velocidade (km/h)')
    axes[i].legend()
    axes[i].grid()

# Configurando o rótulo comum do eixo X
plt.xlabel('Frame')

# Ajustando os espaçamentos entre os subgráficos
plt.tight_layout()

# Exibindo o gráfico
plt.show()
