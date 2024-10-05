import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the dataset
methane_stat_file = pd.read_csv("D:\\planet dynamics\\methane_data.csv")

# Extract data
x = methane_stat_file["year"]
y = methane_stat_file["average"]

# Define a function to map y-values to colors
def get_color(y_value):
    if 1600 <= y_value <= 1700:
        return 'green'
    elif 1700 < y_value <= 1750:
        return 'indigo'
    elif 1750 < y_value <= 1800:
        return 'black'
    elif 1800 < y_value <= 1850:
        return 'orange'
    elif 1850 < y_value <= 2000:
        return 'red'
    else:
        return 'gray'  # Default color for values outside the range

# Create figure and axis
plt.figure()
plt.xlim(x.min(), x.max())
plt.ylim(y.min() - 0.1, y.max() + 0.1)
plt.xlabel("Years")
plt.ylabel("CH4 (Parts Per Billion)")
plt.title("Monthly mean CH4 constructed from daily mean values.")

# Update function to change the scatter plot data
def update(frame):
    plt.cla()  # Clear current axes
    colors = [get_color(val) for val in y[:frame]]  # Get colors for each y value
    plt.scatter(x[:frame], y[:frame], c=colors,marker="+")  # Update scatter points with colors
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min() - 0.2, y.max() + 0.1)
    plt.xlabel("Year")
    plt.ylabel("CH4 (Parts Per Billion)")
    plt.title("Monthly mean CH4 constructed from daily mean values.")

# Create animation
#ani = FuncAnimation(plt.gcf(), update, frames=len(x), interval=1)
update(len(x))
plt.grid()
plt.show()
