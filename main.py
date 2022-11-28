import random
from math import gcd


def lenstra(n):
    g = n
    while g == n & g > 1:
        x, y, a = random.randint(0, n - 1)
        b = (y ^ 2 - x ^ 3 - a * x) % n
        g = gcd(n, 4 * a ^ 3 + 27 * b ^ 2)
    B = random.randint(1, n - 1)
    P = [x, y]


if __name__ == '__main__':
    lenstra(455839)
