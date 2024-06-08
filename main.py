from scipy.stats import binom, geom, poisson, mode
import numpy as np
import matplotlib.pyplot as plt

sizes = [10**2, 10**3, 10**4, 10**5]

# Datos para Distribución Binomial.
n = 100
p = 0.35
binom_dist = binom(n, p)

# Datos para Distribución Geométrica.
pgeom = 0.08
geom_dist = geom(pgeom)

# Datos para Distribución de Poisson.
L = 30
poisson_dist = poisson(L)

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


# Calcula estadísticas descriptivas para los datos proporcionados.
def calculate_statistics(data, distribution_type):
    median = np.median(data)
    mode_value = mode(data)[0]
    mean = np.mean(data)
    variance = np.var(data)

    calculation_functions = {
        'Binomial': calculate_statistics_binom,
        'Geométrica': calculate_statistics_geom,
        'Poisson': calculate_statistics_poisson
    }

    if distribution_type in calculation_functions:
        expected_value, theoretical_variance = calculation_functions[distribution_type]()
    else:
        expected_value, theoretical_variance = None, None

    return median, mode_value, mean, variance, expected_value, theoretical_variance

def calculate_statistics_binom():
    binom_expected_value = binom_dist.mean()
    binom_theoretical_variance = binom_dist.var()
    return binom_expected_value, binom_theoretical_variance

def calculate_statistics_geom():
    geom_expected_value = geom_dist.mean()
    geom_theoretical_variance = geom_dist.var()
    return geom_expected_value, geom_theoretical_variance

def calculate_statistics_poisson():
    poisson_expected_value = poisson_dist.mean()
    poisson_theoretical_variance = poisson_dist.var()
    return poisson_expected_value, poisson_theoretical_variance

# Añade un cuadro de texto con estadísticas a un gráfico.
def add_statistics_text(ax, statistics):
    median, mode_value, mean, variance, expected_value, theoretical_variance = statistics
    text_str = '\n'.join((
        f'Mediana: {median:.2f}',
        f'Moda: {mode_value:.2f}',
        f'Media: {mean:.2f}',
        f'Varianza: {variance:.2f}',
        f'Esperanza Teórica: {expected_value:.2f}',
        f'Varianza Teórica: {theoretical_variance:.2f}'))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, text_str, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)


# Genera un diagrama de cajas a partir de las muestras obtenidas.
def generate_box_diagram(samples, distribution_type):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, size in enumerate(sizes):
        ax = axes[i]
        ax.boxplot(samples[size])
        ax.set_title(f'Distribución {distribution_type} con tamaño = {size}')
        statistics = calculate_statistics(samples[size], distribution_type)
        add_statistics_text(ax, statistics)

    plt.tight_layout()
    plt.show()


# Genera un histograma a partir de las muestras obtenidas.
def generate_histogram(samples, distribution_type):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, size in enumerate(sizes):
        ax = axes[i]
        ax.hist(samples[size], bins=15)
        ax.set_title(f'Distribución {distribution_type} con tamaño = {size}')
        statistics = calculate_statistics(samples[size], distribution_type)
        add_statistics_text(ax, statistics)

    plt.tight_layout()
    plt.show()


def main():
    # Ejercicio 1
    samples_binom = generate_random_samples_binom()
    generate_box_diagram(samples_binom, 'Binomial')
    generate_histogram(samples_binom, 'Binomial')

    # Ejercicio 2
    samples_geom = generate_random_samples_geom()
    generate_box_diagram(samples_geom, 'Geométrica')
    generate_histogram(samples_geom, 'Geométrica')

    # Ejercicio 3
    samples_poisson = generate_random_samples_poisson()
    generate_box_diagram(samples_poisson, 'Poisson')
    generate_histogram(samples_poisson, 'Poisson')


if __name__ == "__main__":
    main()
