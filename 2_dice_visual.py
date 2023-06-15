from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

dice_1 = Dice(6)
dice_2 = Dice(6)

results = []
for roll_num in range(10000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

max_result = dice_1.num_sides + dice_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# The parameter 'dtick': 1 instructs Plotly to label all tick marks.
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')