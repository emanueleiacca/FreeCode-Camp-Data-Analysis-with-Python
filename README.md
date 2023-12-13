# Mean-Variance-Standard-Deviation-Calculator
This is a Python project that calculates the mean, variance, standard deviation, maximum, minimum, and sum of a 3x3 matrix using NumPy.

## Project Overview

The Mean-Variance-Standard Deviation Calculator is designed to take a list of 9 digits as input and perform various calculations on the elements of a 3x3 matrix. The calculations include the mean, variance, standard deviation, maximum, minimum, and sum along both axes (rows and columns) and for the flattened matrix.

## Example
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

output:{

'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],

'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],

'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],

'max': [[6, 7, 8], [2, 5, 8], 8],

'min': [[0, 1, 2], [0, 3, 6], 0],

'sum': [[9, 12, 15], [3, 12, 21], 36]
}
# Demographic-Data-Analyzer
This project analyzes demographic data using Pandas. The dataset used in this project is extracted from the 1994 Census database.

## Dataset

The dataset used for analysis is stored in the `adult.data.csv` file. It contains demographic information such as age, workclass, education, marital status, occupation, race, sex, capital gain/loss, hours per week, native country, and salary.

## Project Description

The `demographic_data_analyzer.py` script performs various calculations and data manipulations to answer the following questions:

1. How many people of each race are represented in this dataset?
2. What is the average age of men?
3. What is the percentage of people who have a Bachelor's degree?
4. What percentage of people with advanced education make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
8. What country has the highest percentage of people that earn >50K and what is that percentage?
9. Identify the most popular occupation for those who earn >50K in India.

# Medical-Data-Visualizer
## Tasks
The project includes the following tasks:

Drawing a categorical plot:

Create a chart showing the counts of variables for patients with different cardio values.

Normalize the data and plot the counts for cholesterol and glucose variables using Seaborn's countplot.

![Figure_1](https://github.com/emanueleiacca/Medical-Data-Visualizer/assets/128679981/3d7be071-7673-4520-9008-91ac52aa5247)


Cleaning the data and creating a correlation matrix:

Clean the data by filtering out incorrect patient segments.

Calculate the correlation matrix using Pandas' corr() function.

Create a correlation matrix heatmap using Seaborn's heatmap() function.

![Figure_2](https://github.com/emanueleiacca/Medical-Data-Visualizer/assets/128679981/92a4ee18-b826-410d-83bf-2d03587acf6b)

# Page-View-Time-Series-Visualizer
This project visualizes time series data using line charts, bar charts, and box plots. It uses Pandas, Matplotlib, and Seaborn to analyze and plot the number of page views on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.

## draw_line_plot():
The draw_line_plot() function reads the dataset from the "fcc-forum-pageviews.csv" file and filters out extreme values. It then plots a line chart using Matplotlib to visualize the daily page views over time.

![SEEVV](https://github.com/emanueleiacca/Page-View-Time-Series-Visualizer/assets/128679981/45af551c-4b1c-4217-9b7f-9c6360a59828)


The x-axis represents the date, and the y-axis represents the page views. The chart shows the trend of page views from May 2016 to December 2019. The title of the chart is "Daily freeCodeCamp Forum Page Views 5/2016-12/2019".

## draw_bar_plot():
The draw_bar_plot() function reads the dataset from the "fcc-forum-pageviews.csv" file and calculates the average daily page views for each month grouped by year. It then plots a bar chart using Matplotlib to visualize the average page views per month.

![zdgzrhgz2](https://github.com/emanueleiacca/Page-View-Time-Series-Visualizer/assets/128679981/f7f699f6-2fa5-4194-b4b1-7628e9de95dd)


The x-axis represents the years, and the y-axis represents the average page views. Each bar in the chart represents a month, and the height of the bar represents the average page views for that month. The legend on the chart shows the month labels, and the title of the legend is "Months". The x-axis is labeled as "Years", and the y-axis is labeled as "Average Page Views".

## draw_box_plot():
The draw_box_plot() function reads the dataset from the "fcc-forum-pageviews.csv" file and calculates the average page views for each year and month. It then plots two adjacent box plots using Seaborn to visualize the distribution of page views within a given year and month and how it compares over time.

![bzbzd3](https://github.com/emanueleiacca/Page-View-Time-Series-Visualizer/assets/128679981/3926d1c9-1fa2-45f5-9c24-3e688bca5e1f)


The first box plot represents the year-wise distribution of page views. The x-axis represents the years, and the y-axis represents the page views. The title of the first chart is "Year-wise Box Plot (Trend)".

The second box plot represents the month-wise distribution of page views. The x-axis represents the months, and the y-axis represents the page views. The title of the second chart is "Month-wise Box Plot (Seasonality)". The x-axis labels start from January, and the x and y axes are labeled correctly.

# Sea-Level-Predictor
This project analyzes a dataset of global average sea level change since 1880 and predicts the sea level change through the year 2050. It utilizes data analysis techniques, including data importation, visualization, and linear regression, to provide insights into the sea level rise.

## Project Tasks
The project tasks include:

Importing the sea level data using Pandas.

Creating a scatter plot of the sea level data.

Calculating the slope and y-intercept of the line of best fit using the linregress function.

Plotting the line of best fit over the scatter plot, extending to the year 2050.

Plotting a new line of best fit using data from the year 2000 onwards, extending to the year 2050.

Adding labels and a title to the plot.

## Final Results

![XF XV](https://github.com/emanueleiacca/Sea-Level-Predictor/assets/128679981/bf71aeec-e444-4e41-9e2d-bdab6e676c54)
