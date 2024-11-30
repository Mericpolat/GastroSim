import numpy as np
from foodsim.heat_transfer import heat_transfer
from foodsim.mass_transfer import mass_transfer
from foodsim.chemical_reactions import chemical_reaction_rate
from foodsim.visualization import plot_results

# Parameters
temp_initial = np.zeros(100)
temp_initial[50] = 100  # Initial temperature at the center
thermal_diffusivity = 0.01
dx = 0.1
dt = 0.01
steps = 500

# Simulate heat transfer
temperature = heat_transfer(temp_initial, thermal_diffusivity, dx, dt, steps)

# Visualize results
plot_results(temperature, "Heat Transfer Simulation", "Position", "Temperature")

# Simulate chemical reaction
concentration = np.ones(100) * 1.0
reaction_rate = 0.02
steps = 100
final_concentration = chemical_reaction_rate(concentration, reaction_rate, steps)

# Visualize results
plot_results(final_concentration, "Chemical Reaction Simulation", "Time", "Concentration")