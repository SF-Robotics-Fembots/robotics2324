import pandas as pd
import csv
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# Make a list of columns
columns = ['receiver 1', 'receiver 2', 'receiver 3']

# change the filename to where the actual data is stored
df = pd.read_csv("C:/Users/kthog/Downloads/csv data prep table - Sheet1.csv", usecols=columns)

# Plot the lines

df.plot(color=['#6495F2', '#06A6AB', '#34E9D5'])

plt.title("Number of Sturgeon detected at each receiver over time")


plt.xlabel("Time (day)")
plt.ylabel("# of sturgeon")


plt.show()