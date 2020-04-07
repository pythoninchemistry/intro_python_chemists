import matplotlib.pyplot as plt
import numpy as np

def plot_wavefunction(n,L):
    """
    Plot a particle in a box wavefunction

    Args:
    n (int): the principle quantum number
    L (float): the length of the box

    Returns:
    Plots the wavefunction
    """
    x = np.linspace(0, L, 1000)
    psi = np.sqrt(2 / L) * np.sin((n * np.pi * x) / L)
    plt.plot(x, psi, label = "n = {}".format(n))
    plt.xlabel(r"x")
    plt.ylabel(r"$\Psi(x)$")
    plt.legend()
    plt.hlines(0,0,L, linestyle = 'dotted')
    plt.xlim(0,L)
