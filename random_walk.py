from random import choice

class RandomWalk():
    """The class for generating random walks."""

    def __init__(self, num_points = 10000):
        """Initializes the attributes of a random walk."""
        self.num_points = num_points

        # All random walks started at the point (0.0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Computes all the points of the random walk."""

        #The steps are generated until the desired length is reached.
        while len(self.x_values) < self.num_points:

            x_step = self._get_step()
            y_step = self._get_step()

            #Ignoring of zero mooves
            if x_step == 0 and y_step == 0:
                continue

            #Computing the next values of x and y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        """Calculating the step."""

        # Determining the direction and length of movement.
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
        step = direction * distance

        return step



