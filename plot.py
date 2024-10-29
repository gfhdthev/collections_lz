import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 3*x**2 + 2*x #устанавливаем функцию 3 степени

x = np.linspace(-2, 4, 40)  # генерируем 40 точек от -2 до 4
y = f(x) #используя фенкцию устанавливаем координаты y

# Создаем график
plt.plot(x, y, label='f(x) = x^3 - 3x^2 + 2x', color='blue') #создаем пометку 
plt.title('График функции y') #подписываем весь график
plt.xlabel('Ось x') #подписываем ось x
plt.ylabel('Ось y') #подписываем ось y

plt.grid() #устанавливаем сетку, чтобы лучше ориентироваться

plt.xlim(-2, 4) #устанавливаем изначальный вид функции
plt.ylim(-10, 10) 

plt.show() #выводим график