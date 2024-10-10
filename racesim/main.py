from tire import Tire
from racesim import RaceSim

import numpy as np
import matplotlib.pyplot as plt

soft = Tire(78, 0.2, 20, "soft")
medium = Tire(79.6, 0.09, 37, "medium")
hard = Tire(80.8, 0.04, 50, "hard")

laps = 72

race = RaceSim(laps)

results = race.optimize(soft, [soft, medium, hard], 2)

#print(results)



#print(race.simulate(soft, [22, 80], [medium, soft], print_laps=True))

"""

x = np.arange(1, laps+1)
y1 = [race.simulate(soft, i, hard) for i in x]
y2 = [race.simulate(soft, i, medium) for i in x]
y3 = [race.simulate(soft, i, soft) for i in x]

plt.plot(x, y1, label="Hard")
plt.plot(x, y2, label="Medium")
plt.plot(x, y3, label="Soft")
plt.legend()
plt.show()

xd = np.arange(1, 61)
yd = [soft.laptime(i)[0] for i in xd]

xd2 = np.arange(1, 61)
yd2 = [medium.laptime(i)[0] for i in xd2]

xd3 = np.arange(1, 61)
yd3 = [hard.laptime(i)[0] for i in xd3]

plt.plot(xd, yd, label="Soft")
plt.plot(xd2, yd2, label="Medium")
plt.plot(xd3, yd3, label="Hard")
plt.legend()
plt.show()


"""