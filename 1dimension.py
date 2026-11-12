import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


length = int(input("Введите длину колбы (от 1000 до 3000): "))
temperature = int(input("Введите комнатную температуру (в кельвинах до 500): "))
material = input("Выберите вещество (азот, водород или кислород): ")
materials = ["азот", "водород", "кислород"]
if (type(temperature) != int or type(length) != int or length < 1000 or length > 3000 or temperature < 0 or temperature > 500
        or material not in materials or type(material) != str):
    print("Что ж, видимо, вы не хотите посмотреть движение частицы.")
else:
    N = int(input("Введите количество молекул (не больше 10): "))
    print("Теперь для каждой из молекул введите её координаты, попадающие в диапозон и с точностью до знака: ")
    points = []
    for i in range(N):
        point = int(input())
        points.append(point)
    fl = 0
    for j in range(N):
        for k in range(j + 1, N):
            if abs(points[j] - points[k]) < 10:
                fl = 1
                break
    if fl == 1 or N < 0 or N > 10:
        print("Что ж, видимо, вы не хотите посмотреть движение частицы.")
    else:
        colors = ['red', 'blue', 'green', 'yellow', 'black', 'orange', 'purple', 'brown', 'gray', 'pink']
        n = 10000
        k = 1.38
        if material == "азот":
            m = 14
        elif material == "водород":
            m = 2
        else:
            m = 32
        dt = 3 * k * temperature / m
        fig, ax = plt.subplots(figsize=(12, 1))
        ax.set_xlim(-length / 2, length / 2)
        ax.set_yticks([])
        points_ax = [0] * (N)
        for i in range(N):
            points_ax[i], = ax.plot([], [], 'o', c = colors[i], ms = 15)
        ds = []
        for i in range(N):
            ds.append([0] * (n + 1))
            ds[i][0] = points[i]
        dr = np.zeros(N)
        for i in range(n):
            for j in range(N):
                dr[j] = np.random.normal(0, np.sqrt(dt))
                ds[j][i + 1] = ds[j][i] + dr[j]
                if ds[j][i + 1] < -length / 2 + 5:
                    ds[j][i + 1] = -length + 10 - ds[j][i + 1]
                    dr[j] = -dr[j]
                if ds[j][i + 1] > length / 2 - 5:
                    ds[j][i + 1] = length - 10 - ds[j][i + 1]
                    dr[j] = -dr[j]
            for j in range(N):
                for k in range(j + 1, N):
                    if abs(ds[j][i + 1] - ds[k][i + 1]) < 10 or (ds[j][i + 1] - ds[k][i + 1]) * (ds[j][i] - ds[k][i]) < 0:
                        if ds[j][i + 1] < -length / 2 + 5 or ds[j][i + 1] > length / 2 - 5:
                            ds[j][i + 1] = ds[j][i]
                            dr[j] = 0
                            ds[k][i + 1] = ds[k][i] - dr[k]
                            dr[k] = -dr[k]
                        elif ds[k][i + 1] < -length / 2 + 5 or ds[k][i + 1] > length / 2 - 5:
                            ds[k][i + 1] = ds[k][i]
                            dr[k] = 0
                            ds[j][i + 1] = ds[j][i] - dr[j]
                            dr[j] = -dr[j]
                        else:
                            ds[j][i + 1] = ds[j][i] - dr[j]
                            ds[k][i + 1] = ds[k][i] - dr[k]
                            dr[j] = -dr[j]
                            dr[k] = -dr[k]


        def up(i):
            for j in range(N):
                points_ax[j].set_data([ds[j][i]], [0])
            return points_ax


        ani = animation.FuncAnimation(fig, up, frames = n + 1, interval = 30, blit = True)
        plt.show()