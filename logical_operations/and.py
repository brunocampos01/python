import matplotlib.pyplot as plt
import numpy as np


def and_operation(x1, x2):
    i = np.array([x1, x2])
    # Wegith and threshold is defined manually for correct AND
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(i * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


X = [[0, 0], [0, 1], [1, 0], [1, 1]]

for x in X:
    y = and_operation(x[0], x[1])
    color = None
    if y == 0:
        color = "b"
    else:
        color = "r"
    plt.plot(x[0], x[1], "o" + color)

# Dividing line
eq = lambda _x: -_x + 1.2
x1 = [i * 0.1 for i in range(-4, 14)]
y1 = list(map(eq, x1))
plt.plot(x1, y1, "g")

plt.grid()
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.title("AND")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()
