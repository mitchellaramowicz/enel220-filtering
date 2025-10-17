import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

R = 89 # 89 Ohms
L = 0.281 # 0.281 H
C = 10e-9 # 10 nF

f0 = 1000 # 1 KHz
V_peak = 5 # 5 V
period = 1 / f0

num_periods = 5
t = np.linspace(0, num_periods * period, 10000)

u = (V_peak / 2) * (signal.square(2 * np.pi * f0 * t) + 1)

num = [R * C, 0]
den = [L * C, R * C, 1]
sys = signal.lti(num, den)

t_out, y_out, x_out = signal.lsim(sys, u, t)

plt.figure(figsize=(10, 6))
plt.plot(t * 1000, u, label = "input", color = "blue")
plt.plot(t * 1000, y_out, label = "output", color = "red")
plt.xlabel("time (ms)")
plt.ylabel("voltage (V)")
plt.legend()
plt.grid()
plt.show()