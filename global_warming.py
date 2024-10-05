import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the dataset
heat_file = pd.read_csv("D:/planet dynamics/gobal_temp.csv")

# Extract data
x = heat_file["Year"]
y = heat_file["Anomaly"]

# Define a function to map y-values to colors
def get_color(y_value):
    if -3 <= y_value <= -2:
        return 'green'
    elif -2 < y_value <= -1:
        return 'indigo'
    elif -1 < y_value <= 0:
        return 'black'
    elif 0 < y_value <= 1:
        return 'orange'
    elif 1 < y_value <= 2:
        return 'red'
    else:
        return 'gray'  # Default color for values outside the range

# Create figure and axis
plt.figure()
plt.xlim(x.min(), x.max())
plt.ylim(y.min() - 0.1, y.max() + 0.1)
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Anomaly Over Time")

# Update function to change the scatter plot data
def update(frame):
    plt.cla()  # Clear current axes
    colors = [get_color(val) for val in y[:frame]]  # Get colors for each y value
    plt.scatter(x[:frame], y[:frame], c=colors, marker="^")  # Update scatter points with colors
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min() - 0.2, y.max() + 0.1)
    plt.xlabel("Year")
    plt.ylabel("Temperature Anomaly (°C)")
    plt.title("Global Temperature Anomaly Over Time")
    plt.grid(True)  # Re-add grid after clearing axes

# Create animation with a proper interval (e.g., 50 milliseconds)
ani = FuncAnimation(plt.gcf(), update, frames=len(x), interval=50)

plt.show()
