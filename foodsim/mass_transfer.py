import numpy as np

def mass_transfer(conc_initial, diffusion_coefficient, dx, dt, steps):
    """
    Simulates mass transfer using the diffusion equation.
    """
    conc = np.copy(conc_initial)
    for _ in range(steps):
        conc[1:-1] = conc[1:-1] + diffusion_coefficient * dt / dx**2 * (conc[:-2] - 2*conc[1:-1] + conc[2:])
    return conc