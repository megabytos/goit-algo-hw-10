import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate


def draw(f, a, b, n=1000):
    x = np.linspace(a - 0.5, b + 0.5, n)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y)])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Integral of $x^3 + 3*x^2 + x + 2$ between {a} and {b}')
    plt.grid()
    plt.show()


def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return area


if __name__ == "__main__":

    def f(x):
        return x ** 3 + 3 * x ** 2 + x + 2

    a = -2
    b = 1
    y_min = 0
    y_max = 7
    result_integral, err = integrate.quad(f, a, b)
    print(f"Integral of x^3 + 3*x^2 + x + 2 between {a} and {b} = {result_integral}")
    print(f"Monte Carlo integral (1 000 points) = {monte_carlo_integrate(f, a, b, y_min, y_max, 1000)}")
    print(f"Monte Carlo integral (1 000 000 points) = {monte_carlo_integrate(f, a, b, y_min, y_max, 1000000)}")

    draw(f, a, b, 10000)
    