import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
file = np.genfromtxt("U.S. Standard Atmosphere Air Properties - Imperial (BG) Units.txt", skip_header=2)

h = file[:, 0]*0.3048             # converting ft to m
T = (file[:, 1] + 459.67)*(5/9)     # converting F to K


def temp_curve(x, a, b, c, d, e): return a*x**4 + b*x**3 + c*x**2 + d*x + e


plt.scatter(h, T, label='data', color='blue')
popt, pcov = curve_fit(temp_curve, h, T)
plt.plot(h, temp_curve(h, *popt), 'r--', label=r'fit: $ah^4 + bh^3 + ch^2 + dh + e$')
plt.legend()

plt.ylabel(r"$T(h)$", fontsize=25)
plt.xlabel(r"$h$", fontsize=25)

plt.tight_layout()
plt.show()


print('   a =', '%0.18f' % popt[0])
print('   b =', "%0.18f" % popt[1])
print('   c =', "%0.18f" % popt[2])
print('   d =', '%0.18f' % popt[3])
print('   e =', "%0.18f" % popt[4])


# CONCLUSTION: 𝘛(𝘩) = 0.000000000000000027𝘩^4 - -0.000000000006074933𝘩^3 + 0.000000422889669793𝘩^2 - 0.009918936624872612𝘩 + 289.661267963331567898
