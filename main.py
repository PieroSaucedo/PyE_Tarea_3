from scipy.stats import binom, mode
import numpy as np
import matplotlib.pyplot as plt

n = 100
p = 0.35
sizes = [10**2, 10**3, 10**4, 10**5]

def generate_random_samples():
    samples = {}
    for size in sizes:
        samples[size] = binom.rvs(n, p, size=size)
    return samples

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

def calculate_statistics(samples):
    for size in sizes:
        sample = samples[size]
        print(f'Para la muestra de tamaño {size}:')
        print(f' - Mediana: {np.median(sample)}')
        print(f' - Moda: {mode(sample)[0][0]}')
        print(f' - Media empírica: {np.mean(sample)}')
        print(f' - Varianza empírica: {np.var(sample)}')

def main():
    samples = generate_random_samples()
    generate_box_diagram(samples)
    generate_histogram(samples)
    calculate_statistics(samples)

if __name__ == "__main__":
    main()
