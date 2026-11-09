import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


length = int(input("Введите длину колбы (от 1000 до 3000): "))
height = int(input("Введите высоту колбы (от 1000 до 3000): "))
temperature = int(input("Введите комнатную температуру (в кельвинах до 500): "))
material = input("Выберите вещество (азот или кислород): ")
print("Теперь для каждой из 2 молекул введите её координаты, попадающие в диапозон и с точностью до знака: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (type(temperature) != int or type(length) != int or type(height) != int or height > 3000 or height < 1000
        or length < 1000 or length > 3000 or temperature < 0 or temperature > 500 or (material != "азот" and material != "кислород")
        or type(material) != str or c <= -height / 2 or d <= -height / 2 or a <= -length / 2 or b <= -length / 2
        or c >= height / 2 or d >= height / 2 or a >= length / 2 or b >= length / 2 or type(a) != int or type(b) != int
        or abs(a - c) < 10 or type(c) != int or type(d) != int or abs(b - d) < 10):
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
    else:
        m = 32
    dt = 3 * k * temperature / m
    ds = np.random.normal(0, np.sqrt(dt), n)
    s = np.concatenate([[a], np.cumsum(ds) + a])
    ds1 = np.random.normal(0, np.sqrt(dt), n)
    s1 = np.concatenate([[b], np.cumsum(ds1) + b])
    dr = np.random.normal(0, np.sqrt(dt), n)
    r = np.concatenate([[c], np.cumsum(dr) + c])
    dr1 = np.random.normal(0, np.sqrt(dt), n)
    r1 = np.concatenate([[d], np.cumsum(dr1) + d])
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.set_xlim(-length / 2, length / 2)
    ax.set_ylim(-height / 2, height / 2)
    point1, = ax.plot([], [], 'go', ms = 15)
    point2, = ax.plot([], [], 'ro', ms = 15)


    def up(i):
        point1.set_data([s[i]], [s1[i]])
        point2.set_data([r[i]], [r1[i]])
        return point1, point2


    ani = animation.FuncAnimation(fig, up, frames = n + 1, interval = 30, blit = True)
    plt.show()