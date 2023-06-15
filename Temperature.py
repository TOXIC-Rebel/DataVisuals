import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/NORMAL_DLY_sample_csv.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Reading temperature maximums and dates.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], "%Y%m%d")
        high = int(row[7])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plotting data on a diagram.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
# The argument "alpha" determines the degree of transparency of the output.
# Where 0 is full transparency and 1 (by default) — full opacity.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatting the diagram.
plt.title("Daily high & low temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
# Displaying date labels diagonally.
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()