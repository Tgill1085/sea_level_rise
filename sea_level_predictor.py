import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # set axis of y and x
    y = df["CSIRO Adjusted Sea Level"]
    x = df["Year"]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)


    # Create first line of best fit
    # give the line the two values to work with, and then plot
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred, y_pred, "r")

    # Create second line of best fit
    # start the new line at 2000
    new_df = df.loc[df['Year'] >= 2000]
    # set the axis of x and y for the new line
    new_y = new_df["CSIRO Adjusted Sea Level"]
    new_x = new_df['Year']
    # give the new line two values to work with, then plot
    new_res = linregress(new_x, new_y)
    new_x_pred = pd.Series([i for i in range(2000, 2051)])
    new_y_pred = new_res.slope*new_x_pred + new_res.intercept
    plt.plot(new_x_pred, new_y_pred, 'yellow')

    # Add labels and title
    # set x axis label
    ax.set_xlabel('Year')
    # set y axis label
    ax.set_ylabel('Sea Level (inches)')
    # set title of figure
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
