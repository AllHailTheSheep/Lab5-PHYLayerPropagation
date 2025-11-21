import math

def calculate_received_power_dbm(tx_power_dbm, distance_m, path_loss_exponent_n):
    """
    Calculates the received power in dBm based on the Log-Distance Path Loss model.
    Assumes a reference distance d0=1m and PL(d0)=30dB.

    Args:
        tx_power_dbm (float): Transmitter power in dBm.
        distance_m (float): Distance from transmitter in meters.
        path_loss_exponent_n (float): The path loss exponent (e.g., 2.0 for free space).

    Returns:
        float: The received power in dBm.
    """

    # --- START OF YOUR IMPLEMENTATION ---
    # 1. Define PL_d0 (reference path loss at d0=1m)
    # 2. Calculate the Path Loss (PL) in dB using the formula
    #    PL(dB) = PL(d0) + 10 * n * log10(d / 1)
    # 3. Calculate the Received Power (Pr) in dBm
    #    Pr(dBm) = Ptx(dBm) - PL(dB)

    if distance_m <= 0:
        distance_m = 1.0 # Avoid log(0)

    # Reference path loss at 1 m (given constant for this lab)
    PL_d0_db = 30.0  # dB at d0 = 1 m

    # Path loss
    path_loss_db = PL_d0_db + 10.0 * path_loss_exponent_n * math.log10(distance_m / 1.0)

    # Received power
    pr_dbm = tx_power_dbm - path_loss_db

    return pr_dbm
    # --- END OF YOUR IMPLEMENTATION ---


def calculate_shannon_capacity_bps(bandwidth_hz, received_power_dbm, noise_floor_dbm=-95.0):
    """
    Calculates the theoretical channel capacity using the Shannon-Hartley theorem.

    Args:
        bandwidth_hz (float): Channel bandwidth in Hertz.
        received_power_dbm (float): Received power in dBm.
        noise_floor_dbm (float): Noise floor in dBm (default is -95.0).

    Returns:
        float: The theoretical capacity in bits per second (bps).
    """

    # --- START OF YOUR IMPLEMENTATION ---
    # 1. Convert received_power_dbm (Pr) to milliwatts (mW).
    #    Hint: P(mW) = 10^(P(dBm) / 10)
    # 2. Convert noise_floor_dbm (Pn) to milliwatts (mW).
    # 3. Calculate the linear Signal-to-Noise Ratio (SNR).
    #    SNR = Pr(mW) / Pn(mW)
    # 4. Apply the Shannon formula.
    #    C = B * log2(1 + SNR)
    #    Hint: math.log2(x)

    # If bandwidth is non-positive, no capacity
    if bandwidth_hz <= 0:
        return 0.0

    # Convert dBm to mW safely and calculate noise ratio
    pr_mw = 10 ** (received_power_dbm / 10.0)
    pn_mw = 10 ** (noise_floor_dbm / 10.0)
    snr_linear = pr_mw / pn_mw

    # Capacity in bits per second
    capacity_bps = bandwidth_hz * math.log2(1.0 + snr_linear)

    return capacity_bps
    # --- END OF YOUR IMPLEMENTATION ---


if __name__ == '__main__':
    # This file is intended to be imported as a module, not run directly.
    # You can, however, add your own simple tests here for debugging
    # by calling your functions and printing the results.

    print("phy_model.py is a module and is not intended to be run directly.")
    print("Add your own test cases here if you wish.")

    # Example Test (you can uncomment this to test your code)
    pr_test = calculate_received_power_dbm(tx_power_dbm=20, distance_m=1, path_loss_exponent_n=2.0)
    print(f"Test Pr: {pr_test:.2f} dBm") # Expected: -10.00 dBm

    cap_test = calculate_shannon_capacity_bps(bandwidth_hz=20e6, received_power_dbm=-65.0)
    print(f"Test Cap: {cap_test / 1e6:.2f} Mbps") # Expected: ~199.3 Mbps