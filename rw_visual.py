import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Building a random walk.
rw = RandomWalk(5000)
rw.fill_walk()

#Plotting points on a diagram.
plt.style.use('classic')
fig, ax = plt.subplots()
#Generating a list of size num_points.
point_numbers = range(rw.num_points)
# Get "point_numbers" to "c" to be mapped to colors Blues
# and edgecolor='none' - no patch boundary will be drawn.
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
           edgecolor='none', s=5)

# Highlighting the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
           s=50)

#Removing the display of axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()