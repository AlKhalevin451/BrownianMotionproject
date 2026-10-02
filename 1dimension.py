import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


t = 10
n = 10000
dt = t / n
dk = np.random.normal(0, np.sqrt(dt), n)
k = np.concatenate([[0], np.cumsum(dk)])
#length = int(input("Введите длину колбы (от 10 до 30): "))
#temperature = int(input("Введите комнатную температуру (в кельвинах): "))
#material = input("Выберите вещество (азот или кислород): ")
#N = int(input("Введите количество молекул: "))
#print("Теперь для каждой молекулы введите её координаты, попадающие в диапозон и с точностью до десятой: ")
#a = []
#for i in range(N):
    #q = int(input())
    #a.append(q)


fig, ax = plt.subplots(figsize=(10, 1))
ax.set_xlim(k.min() - 1, k.max() + 1)
ax.set_yticks([])
point, = ax.plot([], [], 'go', ms = 15)


def up(i):
    point.set_data([k[i]], [0])
    return point,


ani = animation.FuncAnimation(fig, up, frames = n + 1, interval = 30, blit = True)
plt.show()