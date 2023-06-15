from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

# Creating a six-sided dice.
dice = Dice()

# Modeling a series of rolls and saving the results in a list.
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# Analysis of results.
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization of results.
x_values = list(range(1, dice.num_sides+1))
#The 'Bar' class from 'Plotly' is used to represent a dataset,
#and it should be enclosed in square brackets when creating the data variable,
#as it allows for multiple elements in the dataset.
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
# The Layout() class returns an object that defines the layout and configuration of the overall chart.
my_layout = Layout(title='Results of rolling one D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# Building a chart and saving it to a file.
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')