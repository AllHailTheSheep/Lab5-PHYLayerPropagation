import numpy

import phy_model
import matplotlib.pyplot as plt
import math

# --- START OF YOUR IMPLEMENTATION ---

# Define a list or dictionary containing the parameters for each technology
# based on the lab instructions and lecture slides.
# Each technology should have:
# - 'name': (e.g., 'WLAN')
# - 'tx_power_dbm': (in dBm)
# - 'bandwidth_hz': (in Hz)
# - 'path_loss_exponent_n': (unitless)
# TECH         tx_power_dbm         bandwidth_hz        path_loss_exponent_n
# WLAN          20                  20e6                2.5
# BLUETOOTH      4                   1e6                 2
# CELLULAR      23                  10e6                3.5

tech_params = [
    # Example for WLAN
    {
        'name': 'WLAN',
        'tx_power_dbm': 20.0,
        'bandwidth_hz': 20e6,
        'path_loss_exponent_n': 2.5
    },
    {
        'name': 'Bluetooth',
        'tx_power_dbm': 4.0,
        'bandwidth_hz': 1e6,
        'path_loss_exponent_n': 2
    },
    {
        'name': 'Cellular',
        'tx_power_dbm': 23.0,
        'bandwidth_hz': 10e6,
        'path_loss_exponent_n': 3.5
    },
]

# TODO: GENERATE DATA
# Define an array of distances (in meters) from 1m to 1000m.
# Use logarithmic spacing to better visualize over orders of magnitude.
# This generates 100 points from 10^0 (=1 m) to 10^3 (=1000 m).
distances = numpy.logspace(0, 3, num=100)


# Create a dictionary to hold your results
results = {}

# Loop through each technology defined in tech_params
for tech in tech_params:
    tech_name = tech['name']
    results[tech_name] = [] # Initialize an empty list for this tech's rates

    # Loop through each distance in the distances array
    for d in distances:
        # 1. Calculate received power in dBm using the LDPL model
        pr_dbm = phy_model.calculate_received_power_dbm(
            tx_power_dbm=tech['tx_power_dbm'],
            distance_m=float(d),
            path_loss_exponent_n=tech['path_loss_exponent_n']
        )

        # 2. Calculate theoretical capacity in bps using Shannon-Hartley
        capacity_bps = phy_model.calculate_shannon_capacity_bps(
            bandwidth_hz=tech['bandwidth_hz'],
            received_power_dbm=pr_dbm
        )

        # 3. Convert capacity from bps to Mbps and append to the results list
        capacity_mbps = capacity_bps / 1e6
        results[tech_name].append(capacity_mbps)


# --- END OF YOUR IMPLEMENTATION ---


# --- START OF PLOTTING  ---

# This part is also for you to implement.
# Use matplotlib.pyplot (aliased as plt) to create the plot.

# 1. Create a new figure
plt.figure()

# 2. Plot each technology's results
plt.semilogx(distances, results['WLAN'], label='WLAN')
plt.semilogx(distances, results['Bluetooth'], label='Bluetooth')
plt.semilogx(distances, results['Cellular'], label='Cellular')

# 3. Add plot labels and a title
plt.xlabel('Distance (meters)')
plt.ylabel('Theoretical Data Rate (Mbps)')
plt.title('Wireless Technology PHY Layer Capacity Comparison')
plt.legend() # Show the legend
plt.grid(True) # Add a grid for readability

# 4. Show the plot
plt.show()

# --- END OF PLOTTING ---

print("Lab 5 simulation complete. Plot should be displayed.")