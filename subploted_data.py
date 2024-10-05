import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the datasets
heat_file = pd.read_csv("E:/NSAC/pd_git/gobal_temp.csv")
co2_stat_file = pd.read_csv("E:/NSAC/pd_git/stat.csv")
methane_stat_file = pd.read_csv("E:/NSAC/pd_git/methane_data.csv")

# Extract data for the first plot (Temperature Anomaly)
x1 = heat_file["Year"]
y1 = heat_file["Anomaly"]

# Extract data for the second plot (CO2 Stats)
x2 = co2_stat_file["Year"]
y2 = co2_stat_file["Monthly_Average"]

# Extract data for the third plot (CH4 Stats)
x3 = methane_stat_file["year"]
y3 = methane_stat_file["average"]

# Define a function to map y-values to colors for both datasets
def get_color_temp(y_value):
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
        return 'gray'

def get_color_co2(y_value):
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
        return 'gray'

def get_color_methane(y_value):
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
        return 'gray'

# Create figure and subplots (1 row, 3 columns)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 7))

# Set properties for the Temperature Anomaly subplot
ax1.set_xlim(x1.min(), x1.max())
ax1.set_ylim(y1.min() - 0.2, y1.max() + 0.1)
ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature Anomaly (°C)")
ax1.set_title("Global Temperature Anomaly Over Time")
ax1.grid(True)

# Set properties for the CO2 Stats subplot
ax2.set_xlim(x2.min(), x2.max())
ax2.set_ylim(y2.min() - 0.2, y2.max() + 0.1)
ax2.set_xlabel("Year")
ax2.set_ylabel("CO2 (Parts Per Million)")
ax2.set_title("Monthly Mean CO2 Values")
ax2.grid(True)

# Set properties for the CH4 Stats subplot
ax3.set_xlim(x3.min(), x3.max())
ax3.set_ylim(y3.min() - 0.2, y3.max() + 0.1)
ax3.set_xlabel("Year")
ax3.set_ylabel("CH4 (Parts Per Billion)")
ax3.set_title("Monthly Mean CH4 Values")
ax3.grid(True)

# Update function for the animation
def update(frame):
    # Temperature Anomaly Animation (Left Plot)
    ax1.cla()
    colors1 = [get_color_temp(val) for val in y1[:frame]]
    ax1.scatter(x1[:frame], y1[:frame], c=colors1, marker="^")
    ax1.set_xlim(x1.min(), x1.max())
    ax1.set_ylim(y1.min() - 0.2, y1.max() + 0.1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Temperature Anomaly (°C)")
    ax1.set_title("Global Temperature Anomaly Over Time")
    ax1.grid(True)

    # CO2 Stats Animation (Middle Plot)
    ax2.cla()
    colors2 = [get_color_co2(val) for val in y2[:frame]]
    ax2.scatter(x2[:frame], y2[:frame], c=colors2, marker="_")
    ax2.set_xlim(x2.min(), x2.max())
    ax2.set_ylim(y2.min() - 0.2, y2.max() + 0.1)
    ax2.set_xlabel("Year")
    ax2.set_ylabel("CO2 (Parts Per Million)")
    ax2.set_title("Monthly Mean CO2 Values")
    ax2.grid(True)

    # CH4 Stats Animation (Right Plot)
    ax3.cla()
    colors3 = [get_color_methane(val) for val in y3[:frame]]
    ax3.scatter(x3[:frame], y3[:frame], c=colors3, marker="+")
    ax3.set_xlim(x3.min(), x3.max())
    ax3.set_ylim(y3.min() - 0.2, y3.max() + 0.1)
    ax3.set_xlabel("Year")
    ax3.set_ylabel("CH4 (Parts Per Billion)")
    ax3.set_title("Monthly Mean CH4 Values")
    ax3.grid(True)

# Create animation with a proper interval
ani = FuncAnimation(fig, update, frames=len(x1), interval=0, repeat=False)

# Display the plots
plt.tight_layout()
plt.show()
