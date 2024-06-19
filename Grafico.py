from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from Lab_incer import *

config_plt = {
  "xtick.top": True,
  "ytick.right": True,
  "xtick.direction": "in",
  "ytick.direction": "in",
  "xtick.labelsize": 12,
  "ytick.labelsize": 12,
  "axes.titlesize": 12,
  "axes.labelsize": 12,
  "legend.fontsize": 12,
  "figure.subplot.wspace": 0.5,
  "figure.subplot.hspace": 0.5,
}
plt.style.use([config_plt])

x = np.array(Lista_kg)
y = np.array(Lista_Dg)
u_x = np.array(Lista_ukg)
u_y = np.array(Lista_ud)

result = stats.linregress(x, y)

# The number of digits printed might need to be ajusted.

print('''f"Linear regression:\n
Slope: {result.slope:.2f}+-{result.stderr:.2f} \n
Intercept: {result.intercept:.2f} +-{result.intercept_stderr:.2f}"
      ''')

fig3, ax3 = plt.subplots(1, 1)
ax3.errorbar(
  x,
  y,
  xerr=u_x,
  yerr=u_y,
  fmt="o",
  elinewidth=1,
  capsize=3,
  capthick=1,
  ms=3,
  c="b",
  ecolor="black",
)
ax3.plot(x, x * result.slope + result.intercept)
ax3.set_xlabel("y (arb.u.)")
ax3.set_ylabel("y (arb. u.)")
plt.show()