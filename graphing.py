import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import random
import sys

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    xar = []
    yar = []
    x = 0
    for val in range(10):
        x += 1
        xar.append(x)
        yar.append(random.randint(1,5))

    print(xar, yar)
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()