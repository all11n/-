import numpy as np
import matplotlib.pyplot as plt

# Коэффициенты квадратного уравнения y = ax^2 + bx + c
print('Введите коэффициент a')
a = float(input())
print('Введите коэффициент b')
b = float(input())
print('Введите коэффициент c')
c = float(input())

# Создаем массив значений x
x = np.linspace(-100, 100, 400)
y = a * x**2 + b * x + c        # Вычисляем y для каждого x

# Строим график
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Линия y = 0
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Линия x = 0


# Настраиваем график
plt.title('График квадратного уравнения')
plt.xlabel('Ox')
plt.ylabel('Oy')
plt.grid(True)
plt.legend()
plt.show()
