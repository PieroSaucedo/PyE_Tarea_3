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


# Calcula las estadisticas esperadas de cualquiera de los tres tipos de
# distribuciones presentadas.
def calculate_expected_statistics(distribution_name):
    match distribution_name:
        case "Binom":
            binom_expected_value = binom_dist.mean()
            binom_theoretical_variance = binom_dist.var()
            return binom_expected_value, binom_theoretical_variance
        case "Geom":
            geom_expected_value = geom_dist.mean()
            geom_theoretical_variance = geom_dist.var()
            return geom_expected_value, geom_theoretical_variance
        case "Poisson":
            poisson_expected_value = poisson_dist.mean()
            poisson_theoretical_variance = poisson_dist.var()
            return poisson_expected_value, poisson_theoretical_variance


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
def calculate_statistics(data):
    median = np.median(data)
    mode_value = mode(data)[0]
    mean = np.mean(data)
    variance = np.var(data)
    return median, mode_value, mean, variance


# Genera un diagrama de cajas a partir de las muestras obtenidas.
def generate_box_diagram(samples, distribution_name):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, size in enumerate(sizes):
        ax = axes[i]
        ax.boxplot(samples[size])
        ax.set_title(f'Distribución {distribution_name} con tamaño = {size}')
        statistics = calculate_statistics(samples[size])
        expected_statistics = calculate_expected_statistics(distribution_name)
        add_statistics_text(ax, statistics, expected_statistics)

    plt.tight_layout()
    plt.show()


# Genera un histograma a partir de las muestras obtenidas.
def generate_histogram(samples, distribution_name):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, size in enumerate(sizes):
        ax = axes[i]
        ax.hist(samples[size], bins=15)
        ax.set_title(f'Distribución {distribution_name} con tamaño = {size}')
        statistics = calculate_statistics(samples[size])
        expected_statistics = calculate_expected_statistics(distribution_name)
        add_statistics_text(ax, statistics, expected_statistics)

    plt.tight_layout()
    plt.show()


# Añade un cuadro de texto con estadísticas a un gráfico.
def add_statistics_text(ax, statistics, expected_statistics):
    median, mode_value, mean, variance = statistics
    expected_value, theoretical_variance = expected_statistics

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


def main():
    # Ejercicio 1
    samples_binom = generate_random_samples_binom()
    generate_box_diagram(samples_binom, "Binom")
    generate_histogram(samples_binom, "Binom")

    # Ejercicio 2
    samples_geom = generate_random_samples_geom()
    generate_box_diagram(samples_geom, "Geom")
    generate_histogram(samples_geom, "Geom")

    # Ejercicio 3
    samples_poisson = generate_random_samples_poisson()
    generate_box_diagram(samples_poisson, "Poisson")
    generate_histogram(samples_poisson, "Poisson")


if __name__ == "__main__":
    main()
