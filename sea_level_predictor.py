import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(14, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended_min = pd.Series(range(df['Year'].min(), 2051))

    sea_levels_predicted_min = intercept + slope * years_extended_min
    plt.plot(years_extended_min, sea_levels_predicted_min)
 

    # Create second line of best fit
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df[df['Year'] >= 2000].Year, df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])

    years_extended_2000 = pd.Series(range(2000, 2051))

    sea_levels_predicted_2000 = intercept2 + slope2 * years_extended_2000
    plt.plot(years_extended_2000, sea_levels_predicted_2000)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()