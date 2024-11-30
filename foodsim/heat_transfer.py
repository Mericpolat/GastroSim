import numpy as np

def heat_transfer(temp_initial, thermal_diffusivity, dx, dt, steps):
    """
    Simulates heat transfer using the Fourier equation.
    """
    temp = np.copy(temp_initial)
    for _ in range(steps):
        temp[1:-1] = temp[1:-1] + thermal_diffusivity * dt / dx**2 * (temp[:-2] - 2*temp[1:-1] + temp[2:])
    return temp