import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(12, 6))

    # Scatter plot of all data
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Line 1: best fit using ALL data, extended to 2050
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = range(df['Year'].min(), 2051)
    ax.plot(years1, [slope1 * y + intercept1 for y in years1], 'r', label='Best Fit Line 1880-2050')

    # Line 2: best fit using data from 2000 onwards, extended to 2050
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years2 = range(2000, 2051)
    ax.plot(years2, [slope2 * y + intercept2 for y in years2], 'g', label='Best Fit Line 2000-2050')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return ax
