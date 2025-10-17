import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

R = 100e3 # 100,000 Ohms
C = 82e-9 # 82 nF

def question_two_b():
    tf = signal.TransferFunction([1], [R * C, 1])
    omega = np.logspace(0, 5, 1000)
    omega, mag, phase = signal.bode(tf, omega)

    # Magnitude plot
    plt.figure(figsize=(8, 4))
    plt.semilogx(omega / (2 * np.pi), mag)
    plt.ylabel("magnitude (dB)")
    plt.xlabel("frequency (Hz)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Phase plot
    plt.figure(figsize=(8, 4))
    plt.semilogx(omega / (2 * np.pi), phase, color = "orange")
    plt.ylabel("phase (degrees)")
    plt.xlabel("frequency (Hz)")
    plt.grid()
    plt.tight_layout()
    plt.show()

def question_two_c():
    data = np.loadtxt("ecg_noisy.txt", skiprows = 1)

    sampling_frequency = 200

    dt = 1 / sampling_frequency
    RC = R * C
    alpha = dt / (RC + dt)

    filtered = np.zeros_like(data)
    filtered[0] = data[0]

    for i in range(1, len(data)):
        filtered[i] = filtered[i - 1] + alpha * (data[i] - filtered[i - 1])

    t = np.arange(len(data)) / sampling_frequency

    plt.figure(figsize=(10, 4))
    plt.plot(t, data, label="original")
    plt.plot(t, filtered, label = "filtered", linewidth = 2)
    plt.xlabel("time (s)")
    plt.ylabel("signal")
    plt.legend()
    plt.show()

    # Calculate RMSE percentage of signal range
    error = filtered - data
    rmse = np.sqrt(np.mean(error ** 2))
    signal_range = np.max(data) - np.min(data)
    rmse_percent = (rmse / signal_range) * 100
    print(f"RMSE: {rmse_percent:.2f}% of signal range")

# Plot magnitude and phase of transfer function
# question_two_b()

# Filtered ECG data
# question_two_c()