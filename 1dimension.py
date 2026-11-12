import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


length = int(input("Введите длину колбы (от 1000 до 3000): "))
temperature = int(input("Введите комнатную температуру (в кельвинах до 500): "))
material = input("Выберите вещество (азот, водород или кислород): ")
print("Теперь для каждой из 2 молекул введите её координаты, попадающие в диапозон и с точностью до знака: ")
a = int(input())
b = int(input())
materials = ["азот", "водород", "кислород"]
if (type(temperature) != int or type(length) != int or length < 1000 or length > 3000 or temperature < 0 or temperature > 500
        or material not in materials or type(material) != str or a < -length / 2 + 5 or b < -length / 2 + 5
        or a > length / 2 - 5 or b > length / 2 - 5 or type(a) != int or type(b) != int or abs(a - b) < 10):
    print("Что ж, видимо, вы не хотите посмотреть движение частицы.")
else:
    #N = int(input("Введите количество молекул: "))
    #a = []
    #for i in range(N):
        #q = int(input())
        #a.append(q)
    n = 10000
    k = 1.38
    if material == "азот":
        m = 14
    elif material == "водород":
        m = 2
    else:
        m = 32
    dt = 3 * k * temperature / m
    s = np.zeros(n + 1)
    r = np.zeros(n + 1)
    ds = 0
    dr = 0
    s[0] = a
    r[0] = b
    fig, ax = plt.subplots(figsize=(12, 1))
    ax.set_xlim(-length / 2, length / 2)
    ax.set_yticks([])
    point1, = ax.plot([], [], 'go', ms = 15)
    point2, = ax.plot([], [], 'ro', ms = 15)
    for i in range(n):
        ds += np.random.normal(0, np.sqrt(dt))
        dr += np.random.normal(0, np.sqrt(dt))
        s[i + 1] = s[i] + ds
        r[i + 1] = r[i] + dr
        if s[i + 1] < -length / 2 + 5:
            s[i + 1] = -length + 10 - s[i + 1]
            ds = -ds
        elif s[i + 1] > length / 2 - 5:
            s[i + 1] = length - 10 - s[i + 1]
            ds = -ds
        if r[i + 1] < -length / 2 + 5:
            r[i + 1] = -length + 10 - r[i + 1]
            dr = -dr
        elif r[i + 1] > length / 2 - 5:
            r[i + 1] = length - 10 - r[i + 1]
            dr = -dr
        if abs(s[i + 1] - r[i + 1]) < 10 or (s[i + 1] - r[i + 1]) * (s[i] - r[i]) < 0:
            s[i + 1] = s[i] - ds
            r[i + 1] = r[i] - dr
            ds = -ds
            dr = -dr


    def up(i):
        point1.set_data([s[i]], [0])
        point2.set_data([r[i]], [0])
        return point1, point2


    ani = animation.FuncAnimation(fig, up, frames = n + 1, interval = 30, blit = True)
    plt.show()