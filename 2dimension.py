import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


length = int(input("Введите длину колбы (от 1000 до 3000): "))
height = int(input("Введите высоту колбы (от 1000 до 3000): "))
temperature = int(input("Введите комнатную температуру (в кельвинах до 500): "))
material = input("Выберите вещество (азот, водород или кислород): ")
print("Теперь для каждой из 2 молекул введите её координаты, попадающие в диапозон и с точностью до знака: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
materials = ["азот", "водород", "кислород"]
if (type(temperature) != int or type(length) != int or type(height) != int or height > 3000 or height < 1000
        or length < 1000 or length > 3000 or temperature < 0 or temperature > 500 or material not in materials
        or type(material) != str or c <= -height / 2 or d <= -height / 2 or a <= -length / 2 or b <= -length / 2
        or c >= height / 2 or d >= height / 2 or a >= length / 2 or b >= length / 2 or type(a) != int or type(b) != int
        or type(c) != int or type(d) != int or ((a - c) ** 2 + (b - d) ** 2 < 100)):
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
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.set_xlim(-length / 2, length / 2)
    ax.set_ylim(-height / 2, height / 2)
    point1, = ax.plot([], [], 'go', ms=5)
    point2, = ax.plot([], [], 'ro', ms=5)
    sx = np.zeros(n + 1)
    sy = np.zeros(n + 1)
    rx = np.zeros(n + 1)
    ry = np.zeros(n + 1)
    sx[0] = a
    sy[0] = b
    rx[0] = c
    ry[0] = d
    for i in range(n):
        ds = np.random.normal(0, np.sqrt(dt))
        dr = np.random.normal(0, np.sqrt(dt))
        phi1 = np.random.uniform(0, 2 * np.pi)
        phi2 = np.random.uniform(0, 2 * np.pi)
        sx[i + 1] = sx[i] + ds * np.cos(phi1)
        sy[i + 1] = sy[i] + ds * np.sin(phi1)
        rx[i + 1] = rx[i] + ds * np.cos(phi2)
        ry[i + 1] = ry[i] + ds * np.sin(phi2)
        fl1 = 0
        fl2 = 0
        if sx[i + 1] < -length / 2 + 5 or sx[i + 1] > length / 2 - 5:
            fl1 += 1
            sx[i + 1] = sx[i]
            sy[i + 1] += ds * np.sin(phi1)
        if sy[i + 1] < -height / 2 + 5 or sy[i + 1] > height / 2 - 5:
            fl1 += 1
            sy[i + 1] = sy[i]
            sy[i + 1] += ds * np.cos(phi1)
        if sx[i + 1] < -length / 2 + 5 or sx[i + 1] > length / 2 - 5:
            fl1 += 1
            sx[i + 1] = sx[i]
            sy[i + 1] += ds * np.sin(phi1)
        if fl1 == 2:
            sx[i + 1] = sx[i] + ds * np.cos(phi1 + np.pi * 1.5)
            sy[i + 1] = sy[i] + ds * np.sin(phi1 + np.pi * 1.5)
        if rx[i + 1] < -length / 2 + 5 or rx[i + 1] > length / 2 - 5:
            fl2 += 1
            rx[i + 1] = rx[i]
            ry[i + 1] += dr * np.sin(phi2)
        if ry[i + 1] < -height / 2 + 5 or ry[i + 1] > height / 2 - 5:
            fl2 += 1
            ry[i + 1] = ry[i]
            ry[i + 1] += dr * np.cos(phi2)
        if rx[i + 1] < -length / 2 + 5 or rx[i + 1] > length / 2 - 5:
            fl1 += 1
            rx[i + 1] = rx[i]
            ry[i + 1] += dr * np.sin(phi2)
        if fl2 == 2:
            rx[i + 1] = rx[i] + dr * np.cos(phi2 + np.pi * 1.5)
            ry[i + 1] = ry[i] + dr * np.sin(phi2 + np.pi * 1.5)
        fl1 = 0
        fl2 = 0
        distance = np.sqrt((rx[i + 1] - sx[i + 1]) ** 2 + (sy[i + 1] - ry[i + 1]) ** 2)
        if distance < 10:
            if abs(phi1 - phi2) == np.pi:
                sx[i + 1] = sx[i]
                sy[i + 1] = sy[i]
                rx[i + 1] = rx[i]
                ry[i + 1] = ry[i]
            else:
                delta = np.sqrt(2) * distance * np.sqrt(1 - np.cos(abs(phi1 - phi2)))
                sx[i + 1] = sx[i] + delta * np.cos(abs(phi1 - phi2))
                sy[i + 1] = sy[i] + delta * np.sin(abs(phi1 - phi2))
                rx[i + 1] = rx[i] + delta * np.cos(abs(phi1 - phi2))
                ry[i + 1] = ry[i] + delta * np.sin(abs(phi1 - phi2))
            if sx[i + 1] < -length / 2 + 5 or sx[i + 1] > length / 2 - 5:
                fl1 += 1
                sx[i + 1] = sx[i]
                sy[i + 1] += ds * np.sin(phi1)
            if sy[i + 1] < -height / 2 + 5 or sy[i + 1] > height / 2 - 5:
                fl1 += 1
                sy[i + 1] = sy[i]
                sy[i + 1] += ds * np.cos(phi1)
            if sx[i + 1] < -length / 2 + 5 or sx[i + 1] > length / 2 - 5:
                fl1 += 1
                sx[i + 1] = sx[i]
                sy[i + 1] += ds * np.sin(phi1)
            if fl1 == 2:
                sx[i + 1] = sx[i] + ds * np.cos(phi1 + np.pi * 1.5)
                sy[i + 1] = sy[i] + ds * np.sin(phi1 + np.pi * 1.5)
            if rx[i + 1] < -length / 2 + 5 or rx[i + 1] > length / 2 - 5:
                fl2 += 1
                rx[i + 1] = rx[i]
                ry[i + 1] += dr * np.sin(phi2)
            if ry[i + 1] < -height / 2 + 5 or ry[i + 1] > height / 2 - 5:
                fl2 += 1
                ry[i + 1] = ry[i]
                ry[i + 1] += dr * np.cos(phi2)
            if rx[i + 1] < -length / 2 + 5 or rx[i + 1] > length / 2 - 5:
                fl1 += 1
                rx[i + 1] = rx[i]
                ry[i + 1] += dr * np.sin(phi2)
            if fl2 == 2:
                rx[i + 1] = rx[i] + dr * np.cos(phi2 + np.pi * 1.5)
                ry[i + 1] = ry[i] + dr * np.sin(phi2 + np.pi * 1.5)



    def up(i):
        point1.set_data([sx[i]], [sy[i]])
        point2.set_data([rx[i]], [ry[i]])
        return point1, point2


    ani = animation.FuncAnimation(fig, up, frames = n + 1, interval = 30, blit = True)
    plt.show()