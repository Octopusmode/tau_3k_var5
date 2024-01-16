import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задание диапазона значений постоянной времени T
T_values = np.linspace(0.1, 1, 20)

# Задание диапазона входного сигнала
input_signal = np.power(np.linspace(1, 10, 20), 2)  # Используем np.power для нелинейного нарастания

# Создание сетки значений T и входного сигнала
T_grid, input_signal_grid = np.meshgrid(T_values, input_signal)

# Расчет амплитуды для каждой комбинации T и входного сигнала
amplitude_grid_integrating = 20 * np.log10(1 / (T_grid * input_signal_grid))
amplitude_grid_differentiating = 20 * np.log10(T_grid * input_signal_grid)  # Добавляем расчет для дифференцирующего звена

# Увеличиваем множитель для выходного сигнала
amplitude_grid_integrating *= 2
amplitude_grid_differentiating *= 2

# Построение 3D-графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T_grid, input_signal_grid, amplitude_grid_integrating, cmap='viridis', alpha=0.5)
ax.plot_surface(T_grid, input_signal_grid, amplitude_grid_differentiating, cmap='plasma', alpha=0.5)  # Добавляем поверхность для дифференцирующего звена

# Добавляем график входного сигнала
ax.plot_surface(T_grid, input_signal_grid, input_signal_grid, cmap='cool', alpha=0.5)

# Настройка осей и заголовка
ax.set_xlabel('Постоянная времени T')
ax.set_ylabel('Входной сигнал')
ax.set_zlabel('Амплитуда (дБ)')
plt.title('Амплитудно-частотная характеристика интегрирующего и дифференцирующего звена')

# Отображение графика
plt.show()