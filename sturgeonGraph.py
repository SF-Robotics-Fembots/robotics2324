import pandas as pd
import csv
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [12, 6]
plt.rcParams["figure.autolayout"] = True

# Make a list of columns
columns = ['Receiver 1', 'Receiver 2', 'Receiver 3']

# change the filename to where the actual data is stored
df = pd.read_csv("C:/Users/kthog/Downloads/csv data prep table - Sheet1.csv", usecols=columns)

# Plot the lines

df.plot(color=['blue', 'red', 'yellow'])

plt.title("Number of Sturgeon detected at each receiver over time")


plt.xlabel("Time (day)")
plt.ylabel("# of sturgeon")


plt.show()