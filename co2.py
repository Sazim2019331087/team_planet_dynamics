import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the dataset
co2_stat_file = pd.read_csv("D:\\planet dynamics\\stat.csv")

# Extract data
x = co2_stat_file["Year"]
y = co2_stat_file["Monthly_Average"]


# Define a function to map y-values to colors
def get_color(y_value):
    if 300 <= y_value <= 340:
        return 'green'
    elif 340 < y_value <= 360:
        return 'indigo'
    elif 360 < y_value <= 380:
        return 'black'
    elif 380 < y_value <= 400:
        return 'orange'
    elif 400 < y_value <= 420:
        return 'red'
    else:
        return 'gray'  # Default color for values outside the range

# Create figure and axis
plt.figure()
plt.xlim(x.min(), x.max())
plt.ylim(y.min() - 0.1, y.max() + 0.1)
plt.xlabel("Years")
plt.ylabel("CO2 (Parts Per Million)")
plt.title("Monthly mean CO2 constructed from daily mean values.")

# Update function to change the scatter plot data
def update(frame):
    plt.cla()  # Clear current axes
    colors = [get_color(val) for val in y[:frame]]  # Get colors for each y value
    plt.scatter(x[:frame], y[:frame], c=colors,marker="_")  # Update scatter points with colors
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min() - 0.2, y.max() + 0.1)
    plt.xlabel("Year")
    plt.ylabel("CO2 (Parts Per Million)")
    plt.title("Monthly mean CO2 constructed from daily mean values.")
    plt.grid()
# Create animation
ani = FuncAnimation(plt.gcf(), update, frames=len(x), interval=50)

plt.show()
