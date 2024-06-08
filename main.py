from scipy.stats import binom, geom, poisson, mode
import numpy as np
import matplotlib.pyplot as plt

sizes = [10**2, 10**3, 10**4, 10**5]

# Datos para Distribución Binomial.
n = 100
p = 0.35

# Datos para Distribución Geométrica.
pgeom = 0.08

# Datos para Distribución de Poisson.
L = 30


# Genera muestras aleatorias con distribución binomial.
def generate_random_samples_binom():
    samples = {}
    for size in sizes:
        samples[size] = binom.rvs(n, p, size=size)
    return samples


# Genera muestras aleatorias con distribución geométrica.
def generate_random_samples_geom():
    samples = {}
    for size in sizes:
        samples[size] = geom.rvs(pgeom, size=size)
    return samples


# Genera muestras aleatorias con distribución de Poisson.
def generate_random_samples_poisson():
    samples = {}
    for size in sizes:
        samples[size] = poisson.rvs(L, size=size)
    return samples


# Genera un diagrama de cajas a partir de las muestras obtenidas.
def generate_box_diagram(samples):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, size in enumerate(sizes):
        axes[i].boxplot(samples[size])
        axes[i].set_title(f'Tamaño de muestra: {size}')

    plt.tight_layout()
    plt.show()


# Genera un histograma a partir de las muestras obtenidas.
def generate_histogram(samples):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, size in enumerate(sizes):
        axes[i].hist(samples[size], bins=15)
        axes[i].set_title(f'Tamaño de muestra: {size}')

    plt.tight_layout()
    plt.show()


# Calcula y muestra en pantalla las diferentes estadísticas requeridas;
# la mediana, moda, media empírica y varianza empírica.
def calculate_statistics(samples):
    for size in sizes:
        sample = samples[size]
        print(f'Para la muestra de tamaño {size}:')
        print(f' - Mediana: {np.median(sample)}')
        print(f' - Moda: {mode(sample)}')
        print(f' - Media empírica: {np.mean(sample)}')
        print(f' - Varianza empírica: {np.var(sample)}')


def main():
    # Ejercicio 1
    samples1 = generate_random_samples_binom()
    generate_box_diagram(samples1)
    generate_histogram(samples1)
    calculate_statistics(samples1)
    
    # Ejercicio 2
    samples2 = generate_random_samples_geom()
    generate_box_diagram(samples2)
    generate_histogram(samples2)
    calculate_statistics(samples2)
    
    # Ejercicio 3
    samples3 = generate_random_samples_poisson()
    generate_box_diagram(samples3)
    generate_histogram(samples3)
    calculate_statistics(samples3)


if __name__ == "__main__":
    main()
