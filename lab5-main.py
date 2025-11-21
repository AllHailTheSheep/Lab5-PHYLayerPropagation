import phy_model
import matplotlib.pyplot as plt
import math

# --- START OF YOUR IMPLEMENTATION ---

# TODO: SET UP TECHNOLOGY PARAMETERS
# Define a list or dictionary containing the parameters for each technology
# based on the lab instructions and lecture slides.
# Each technology should have:
# - 'name': (e.g., 'WLAN')
# - 'tx_power_dbm': (in dBm)
# - 'bandwidth_hz': (in Hz)
# - 'path_loss_exponent_n': (unitless)

tech_params = [
    # Example for WLAN
    {
        'name': 'WLAN',
        'tx_power_dbm': 20.0,
        'bandwidth_hz': 20e6,
        'path_loss_exponent_n': 2.5
    },
    # TODO: Add dictionaries for 'Bluetooth' and 'Cellular'
    {
        'name': 'Bluetooth',
        # ... your parameters here
    },
    {
        'name': 'Cellular',
        # ... your parameters here
    },
]

# TODO: GENERATE DATA
# Define an array of distances (in meters) from 1m to 1000m.
# A list comprehension or numpy.logspace() could be useful here.
# e.g., distances = [i for i in range(1, 1001)]
distances = [] # Placeholder


# Create a dictionary to hold your results
results = {}

# Loop through each technology defined in tech_params
for tech in tech_params:
    tech_name = tech['name']
    results[tech_name] = [] # Initialize an empty list for this tech's rates

    # Loop through each distance in the distances array
    for d in distances:
        # 1. Call calculate_received_power_dbm from phy_model
        #    pass in the correct tx_power, distance, and path_loss_exponent

        # pr_dbm = phy_model.calculate_received_power_dbm(...) # Placeholder

        # 2. Call calculate_shannon_capacity_bps from phy_model
        #    pass in the correct bandwidth and the pr_dbm you just calculated

        # capacity_bps = phy_model.calculate_shannon_capacity_bps(...) # Placeholder

        # 3. Convert capacity from bps to Mbps and append to the results list
        #    for this technology

        pass # Remove this pass when you implement the loop


# --- END OF YOUR IMPLEMENTATION ---


# --- START OF PLOTTING  ---

# This part is also for you to implement.
# Use matplotlib.pyplot (aliased as plt) to create the plot.

# 1. Create a new figure
plt.figure()

# 2. Plot each technology's results
#    plt.semilogx(distances, results['WLAN'], label='WLAN')
#    TODO: Add plots for 'Bluetooth' and 'Cellular'


# 3. Add plot labels and a title
plt.xlabel('Distance (meters)')
plt.ylabel('Theoretical Data Rate (Mbps)')
plt.title('Wireless Technology PHY Layer Capacity Comparison')
plt.legend() # Show the legend
plt.grid(True) # Add a grid for readability

# 4. Show the plot
# plt.show()

# --- END OF PLOTTING ---

print("Lab 5 simulation complete. Plot should be displayed.")