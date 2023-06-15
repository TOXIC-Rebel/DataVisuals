import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth=3)


plt.show()