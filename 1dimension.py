import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


length = int(input("Введите длину колбы (от 10 до 30): "))
temperature = int(input("Введите комнатную температуру (в кельвинах до 500): "))
material = input("Выберите вещество (азот или кислород): ")
if length < 10 or length > 30 or temperature < 0 or temperature > 500 or (material != "азот" and material != "кислород"):
    print("Что ж, видимо, вы не хотите посмотреть движение частицы.")
else:
    #N = int(input("Введите количество молекул: "))
    #print("Теперь для каждой молекулы введите её координаты, попадающие в диапозон и с точностью до десятой: ")
    #a = []
    #for i in range(N):
        #q = int(input())
        #a.append(q)
    n = 10000
    k = 1.38
    if material == "азот":
        m = 16
    else:
        m = 32
    dt = (3 * k * temperature / m) ** 0.5
    ds = np.random.normal(0, np.sqrt(dt), n)
    s = np.concatenate([[0], np.cumsum(ds)])
    fig, ax = plt.subplots(figsize=(length, 1))
    ax.set_xlim(s.min() - 1, s.max() + 1)
    ax.set_yticks([])
    point, = ax.plot([], [], 'go', ms = 15)


    def up(i):
        point.set_data([s[i]], [0])
        return point,


    ani = animation.FuncAnimation(fig, up, frames = n + 1, interval = 30, blit = True)
    plt.show()