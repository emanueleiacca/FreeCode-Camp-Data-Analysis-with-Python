import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the data from the CSV file
    df = pd.read_csv("C:/Users/39388/Downloads/epa-sea-level.csv")

    # Create a scatter plot of the data
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Get the slope, intercept, and other values for the line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create a line of best fit extending to the year 2050
    years_extended = range(1880, 2051)
    line = res.intercept + res.slope * years_extended
    plt.plot(years_extended, line, color='r', label='Best Fit Line')

    # Create a line of best fit for data from year 2000 onwards, extending to the year 2050
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    line_recent = res_recent.intercept + res_recent.slope * years_extended
    plt.plot(years_extended, line_recent, color='g', label='Best Fit Line (2000 onwards)')

    # Set labels and title for the plot
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Add a legend to the plot
    plt.legend()

    # Save and show the plot
    plt.savefig('sea_level_plot.png')
    plt.show()

# Run the function to generate the plot
draw_plot()
