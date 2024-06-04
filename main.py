from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n = 100
p = 0.35
sizes = [102, 103, 104, 105]


def generate_random_samples():
    samples = {}
    for size in sizes:
        samples[size] = binom.rvs(n, p, size=size)


def generate_box_diagram(samples):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, size in enumerate(sizes):
        axes[i].boxplot(samples[size])
        axes[i].set_title(f'Tamaño de muestra: {size}')

    plt.tight_layout()
    plt.show()


def generate_histogram(samples):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, size in enumerate(sizes):
        axes[i].hist(samples[size], bins=15)
        axes[i].set_title(f'Tamaño de muestra: {size}')

    plt.tight_layout()
    plt.show()


def main():
    generate_random_samples()


if __name__ == '__main__':
    main()
