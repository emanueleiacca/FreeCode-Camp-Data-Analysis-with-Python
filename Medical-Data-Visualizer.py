import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Create a chart showing counts of variables for patients with cardio=1 and cardio=0
def draw_cat_plot():
    df = pd.read_csv("C:/Users/39388/Downloads/medical_examination.csv")  
    
    # Create "overweight" column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)
    
    # Normalize data
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    
    # Create subplot chart
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # Plot count plots for cardio=0 and cardio=1 using countplot
    sns.countplot(data=df, x='cholesterol', hue='cardio', ax=axes[0])
    sns.countplot(data=df, x='gluc', hue='cardio', ax=axes[1])
    
    # Set axes labels and titles
    axes[0].set_xlabel('Cholesterol')
    axes[0].set_ylabel('Count')
    axes[0].set_title('Cholesterol Level')
    axes[1].set_xlabel('Glucose')
    axes[1].set_ylabel('Count')
    axes[1].set_title('Glucose Level')
    
    # Show the chart
    plt.show()


# Task 2: Clean the data and create a correlation matrix
def draw_heat_map():
    df = pd.read_csv('C:/Users/39388/Downloads/medical_examination.csv')
    
    # Clean the data
    df = df[(df['ap_lo'] <= df['ap_hi']) &
            (df['height'] >= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975)) &
            (df['weight'] >= df['weight'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975))]
    
    # Calculate correlation matrix
    corr_matrix = df.corr()
    
    # Create a mask for the upper triangle
    mask = np.triu(corr_matrix)
    
    # Set up the heatmap figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create the heatmap
    sns.heatmap(corr_matrix, annot=True, fmt='.1f', mask=mask, cmap='coolwarm', square=True, ax=ax)
    
    # Set the title
    ax.set_title('Correlation Matrix')
    
    # Show the heatmap
    plt.show()


# Run the functions
draw_cat_plot()
draw_heat_map()
