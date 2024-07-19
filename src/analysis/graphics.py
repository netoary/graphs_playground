from resultado_brute import brute
from resultado_angle import angle
from resultado_direct import direct
from resultado_rl import rl

import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
x = [col for col in brute.keys()]

# # Brute
# y_brute = [col[0] for col in brute.values()]
# yerr_brute = [col[1] for col in brute.values()]
# plt.errorbar(x, y_brute, yerr=yerr_brute, label='Brute Method')

# # RL
# y_rl = [col[0] if len(col) > 0 else 0 for col in rl.values()] # TODO AJUSTAR
# yerr_rl = [col[1] if len(col) > 0 else 0 for col in rl.values()]
# plt.errorbar(x, y_rl, yerr=yerr_rl, label='RL Method')

# # Direct
# y_direct = [col[0] if len(col) > 0 else 0 for col in direct.values()]
# yerr_direct = [col[1] if len(col) > 0 else 0 for col in direct.values()]
# plt.errorbar(x, y_direct, yerr=yerr_direct, label='Direct Method')

# # Angle
# y_angle = [col[0] if len(col) > 0 else 0 for col in angle.values()]
# yerr_angle = [col[1] if len(col) > 0 else 0 for col in angle.values()]
# plt.errorbar(x, y_angle, yerr=yerr_angle, label='Angle Method')

## LOG
# Brute
y_brute = [math.log(col[0]) for col in brute.values()]
yerr_brute = [math.log(col[1]) for col in brute.values()]
yerr_brute = [abs(yerr) for yerr in yerr_brute]
plt.errorbar(x, y_brute, yerr=yerr_brute, label='Brute Method')

# RL
y_rl = [math.log(col[0]) if len(col) > 0 else 0 for col in rl.values()] # TODO AJUSTAR
yerr_rl = [math.log(col[1]) if len(col) > 0 else 0 for col in rl.values()]
yerr_rl = [abs(yerr) for yerr in yerr_rl]
plt.errorbar(x, y_rl, yerr=yerr_rl, label='RL Method')

# Direct
y_direct = [math.log(col[0]) if len(col) > 0 else 0 for col in direct.values()]
yerr_direct = [math.log(col[1]) if len(col) > 0 else 0 for col in direct.values()]
yerr_direct = [abs(yerr) for yerr in yerr_direct]
plt.errorbar(x, y_direct, yerr=yerr_direct, label='Direct Method')

# Angle
y_angle = [math.log(col[0]) if len(col) > 0 else 0 for col in angle.values()]
yerr_angle = [math.log(col[1]) if len(col) > 0 else 0 for col in angle.values()]
yerr_angle = [abs(yerr) for yerr in yerr_angle]
plt.errorbar(x, y_angle, yerr=yerr_angle, label='Angle Method')

plt.xlabel("Tipo de Grafo")
# plt.ylabel("Tempo (s)")
plt.ylabel("Tempo log(s)")

plt.legend(loc='lower right')
plt.show()

print('foi')