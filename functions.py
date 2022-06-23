import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


def givens(x, theta):
    plt.clf()
    n = 2  # vector dimension
    y = np.dot(gen_Gmatrix(theta, n), x)
    V = np.stack((x, y))
    origin = np.array([[0, 0], [0, 0]])
    plt.title('Givens')
    plt.quiver(*origin, V[:, 0], V[:, 1], color=['b', 'g'], scale=21)
    plt.show()


def gen_Gmatrix(theta, n):
    Q = np.identity(n)
    for i in range(n):
        for j in range(n):
            if i < j:
                Q[i, j] = -np.sin(theta)
            elif i > j:
                Q[i, j] = np.sin(theta)
            elif i == j:
                Q[i, j] = np.cos(theta)
    return Q


def householder(x, v):
    v = v/la.norm(v)  # unit vector to reflect on its orthogonal subspace
    reflection = x - 2*np.dot(np.dot(x, v), v)
    V = np.stack((v, x, reflection))
    origin = np.array([[0, 0, 0], [0, 0, 0]])

    plt.clf()
    plt.title('Householder')
    plt.axis("equal")

    # subspace orthogonal to v
    plt.plot([0, 1], [0, -(v[0]/v[1])], color='red')
    plt.plot([0, -1], [0, (v[0]/v[1])], color='red')

    plt.quiver(*origin, V[:, 0], V[:, 1], color=['r', 'b', 'g'], scale=21)
    plt.show()
